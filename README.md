# Challenge-API

This is a Local Rest API created for DB migration, this API allows:

- Receive historical data from CSV files.
- Upload these files to the new DataBase.
- Insert batch transactions (1 up to 1000 rows) with one request.

For the correct deployment of this application, you must follow the following steps:

- Download Python, and then in your run the following commands in your terminal:
```
py -m pip install Flask
py -m pip install mysql-connector-python
py -m pip install numpy
py -m pip install pandas 
```
- Download MySQL Server and Connector/Python, you can do this with the following link: https://dev.mysql.com/downloads/mysql/
- Once you do the previous step, you have to create the database and tables, you can do this with the following SQL code:
```
CREATE DATABASE challenge_API;

USE challenge_API;

CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE jobs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    date_time DATETIME,
	department_id INT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    job_id INT NULL,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);
``` 
- Then, go to the database.py file, and put your credencials of your MySQL account (user, password), and the database name.