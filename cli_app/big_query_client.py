import sys
from google.cloud import bigquery

SQL_QUERIES = {
    "1": """
        SELECT
            B.port_name,
            B.country,
            ST_DISTANCE(
                ST_GEOGPOINT(A.port_longitude, A.port_latitude),
                ST_GEOGPOINT(B.port_longitude, B.port_latitude)
            ) AS distance_in_meters
        FROM
            (
              SELECT port_latitude, port_longitude
              FROM `bigquery-public-data.geo_international_ports.world_port_index`
              WHERE port_name LIKE 'JURONG ISLAND'
            ) A,
            (
              SELECT port_name, country, port_latitude, port_longitude
              FROM `bigquery-public-data.geo_international_ports.world_port_index`
              WHERE port_name NOT LIKE 'JURONG ISLAND'
            ) B
        ORDER BY distance_in_meters
        LIMIT 5
    """,
    "2": """
        SELECT country, COUNT(*) AS port_count
        FROM `bigquery-public-data.geo_international_ports.world_port_index`
        WHERE cargo_wharf = TRUE
        GROUP BY country
        ORDER BY port_count DESC
        LIMIT 1
    """,
    "3": """
        SELECT country, port_name, port_latitude, port_longitude
        FROM `bigquery-public-data.geo_international_ports.world_port_index`
        WHERE
          provisions = TRUE
          AND water = TRUE
          AND fuel_oil = TRUE
          AND diesel = TRUE
        ORDER BY ST_DISTANCE(ST_GEOGPOINT(-38.706256, 32.610982), ST_GEOGPOINT(port_longitude, port_latitude))
        LIMIT 1
    """
}


class BigQueryClient:
    def __init__(self, service_account_json_path, dataset):
        self.client = bigquery.Client.from_service_account_json(
            service_account_json_path)
        self.dataset = dataset
        self.dataset_ref = self.client.dataset(self.dataset)

        try:
            self.client.get_dataset(self.dataset_ref)
        except:
            print("Cannot find the dataset."
                  " Please check if the provided dataset name in .env file is correct and try again.")
            sys.exit()

    def does_table_exist(self, table):
        tables = self.client.list_tables(self.dataset_ref)

        for cur_table in tables:
            if cur_table.table_id == table:
                return True

        return False

    def create_table(self, question_number):
        table_name = f"question{question_number}"

        if self.does_table_exist(table_name):
            return f"Failed to create table as another table with the name `{table_name}` already exists in dataset `{self.dataset}`."
        else:
            query = SQL_QUERIES[question_number]
            table_ref = self.dataset_ref.table(table_name)
            job_config = bigquery.QueryJobConfig(
                destination=table_ref, write_disposition="WRITE_TRUNCATE")

            query_job = self.client.query(query, job_config=job_config)
            query_job.result()

            return f"Table `{table_name}` in dataset `{self.dataset}` created successfully."
