# **CLI App**
This is a CLI app built with Python to create BigQuery tables and answer several other questions.

## **Pre installation**
If you do not already have a service account for BigQuery, follow these steps:
1. Create a [Google Cloud Platform](https://cloud.google.com/free/) project.
2. Once you have a project, click on the project dropdown menu and select your project.
3. In the Google Cloud Console sidebar, click on the "IAM & Admin" link.
4. In the IAM & Admin panel, click on "Service accounts".
5. Click on "Create Service Account". Give your service account a name and a description, and click "Create".
6. On the "Grant this service account access to project" screen, select the BigQuery Admin role and click "Continue".
7. Skip the "Grant users access to this service account" screen and click "Done".
8. Your new service account will appear in the list of service accounts. Click on the three-dot menu to the right of your service account and select "Manage Keys".
9. Click on the "Add Key" dropdown and choose "Create new key".
10. Choose JSON as the key type and click "Create". This will download a JSON file containing your service account credentials.

If you do not already have a BigQuery dataset, follow these steps:
1. Open the Google Cloud Console and select your project.
2. In the Google Cloud Console sidebar, click on "BigQuery" to open the BigQuery console.
3. In the left-hand pane, select your project and click on the dropdown arrow next to it.
4. Click "Create dataset" and enter a name for your dataset.
5. Click "Create dataset" to create your dataset.

## **Installation**
1. Clone the application's source code by typing the following command:
```
~$ git clone https://github.com/samtjong23/foodpandaDE.git
```
2. Create a Python 3 (I personally used Python 3.10.6) virtual environment and activate it:
```
~/foodpandaDE$ python3 -m venv ./venv
~/foodpandaDE$ source venv/bin/activate
(venv) ~/foodpandaDE$
```
3. Create a .env file containing your service account JSON file path and BigQuery dataset inside the `foodpandaDE/` directory to access Google API:
```
serviceAccountJsonPath = "{path to service account JSON file}"
bigQueryDataset = "{dataset's name}"
```
4. Install all the dependencies:
```
(venv) ~/foodpandaDE$ python -m pip install -r requirements.txt
```

## **Usage**
1. Once you have run the installation steps, you can type `python -m cli_app` to run the application:
```
(venv) ~/foodpandaDE$ python -m cli_app

Welcome to the CLI App.

Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit
``` 
2. The app has multiple actions and you can perform them by following the given intructions and typing the right option.
3. If you want to create a table, you can type `1`, `2` or `3`:
```
Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit

1

Table `question1` in dataset `{your dataset's name}` created successfully.
```
4. By default a table with the name `question{question number}` will be created (you may open the Google Cloud Console to check if the table has indeed been created). In the event that there already exists another table with the same name, the action will not be performed:
```
Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit

1

Failed to create table as another table with the name `question1` already exists in dataset `foodpandaDataset`.
```
5. If you want to view my answers for the questions not involving table creation, you can type `4` or `5`:
```
Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit

4

Refactoring is the process of restructuring existing code without changing its external behavior. The goal of refactoring can include:
- Improving readability and maintainability
- Reducing complexity
- Improving performance
- Ensuring compatibility with new technologies or platforms

Testing is the process of checking if a software application works as it should. The goal of writing test cases can include:
- Making sure software behaves as expected
- Finding and fixing issues early on
- Ensuring that new changes don't break existing functionality

There are different types of tests, including unit tests and integration tests.
- Unit tests check individual parts of the code in isolation, to ensure they work as intended.
- Integration tests check how different parts of the code work together, to ensure the whole system functions as it should.
```
6. No worries if you provide the wrong input, the app will send you a message to let you know what is happening.
```
Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit

6

Invalid input. Please try again.
```
7. Finally, once you are done you may type `quit` to exit the app:
```
Select action:
* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
* Type `4` to view Samuel's understanding of refactoring and testing
* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
* Type `quit` to exit

quit

Thank you for using the app. Bye. :D
```

## **About the Author**
Samuel Tjong - Email: [samtjong23@gmail.com](mailto:samtjong23@gmail.com)
