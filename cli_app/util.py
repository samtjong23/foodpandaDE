import os
import sys
from dotenv import load_dotenv

from cli_app.big_query_client import BigQueryClient


def get_big_query_client():
    load_dotenv()
    service_account_json_path = os.environ.get("serviceAccountJsonPath")
    dataset = os.environ.get("bigQueryDataset")

    if not service_account_json_path or not dataset:
        print("Some values are missing from the .env file."
              " Please update the file and try again.")
        sys.exit()

    elif not os.path.exists(service_account_json_path):
        print("Cannot find the service account JSON file."
              " Please check if the provided JSON path in .env file is correct and try again.")
        sys.exit()

    else:
        return BigQueryClient(service_account_json_path, dataset)
