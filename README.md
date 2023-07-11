# Challenge-API

This is a Local Rest API created for DB migration, this API allows:

- Receive historical data from CSV files.
- Upload these files to the new DataBase.
- Insert batch transactions (1 up to 1000 rows) with one request.

For the correct deployment of this application, you must follow the following steps:

- Download Python, and the in your run the following commands in your terminal:
```
py -m pip install Flask
py -m pip install mysql-connector-python
py -m pip install numpy
py -m pip install pandas 
```