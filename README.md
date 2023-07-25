# Challenge

## API

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
- To test the application, you can use cURL tool. To use it, you have to download it from the following link: https://curl.se/windows/. Then, extract the downloaded ZIP file, and add the path to the extracted 'curl.exe' file to your system's PATH ENVIRONMENT VARIABLE.
- To run the application, in your terminal you have to write:
```
py app.py
```
- The CSV files are located in the data file. In your terminal, use the following commands to insert the CSV files to the database:
```
curl -X POST -F "file=@C:\path of the project file\data\departments.csv" http://127.0.0.1:5000/upload_deps
curl -X POST -F "file=@C:\path of the project file\data\jobs.csv" http://127.0.0.1:5000/upload_jobs
curl -X POST -F "file=@C:\path of the project file\data\hired_employees.csv" http://127.0.0.1:5000/upload_emp
```
- To insert batch transactions, the API do this with json files. These files are located in the data file too. These files content all the transactions. To test this funcionality you have to run the following comands:
```
curl -X POST -H "Content-Type: application/json" -d  @C:\path of the project file\data\deps.json http://localhost:5000/batch_insert_deps
curl -X POST -H "Content-Type: application/json" -d  @C:\path of the project file\data\hired-emp.json http://localhost:5000/batch_insert_emp
curl -X POST -H "Content-Type: application/json" -d  @C:\path of the project file\data\jobs.json http://localhost:5000/batch_insert_jobs
``` 

## SQL

### Query 1
this query results in the number of employees hired for each job and department in 2021 divided by quarter. The result is ordered alphabetically by department and job. To see the result, write in your terminal:
```
curl http://127.0.0.1:5000/sql_query1
```
This query is created with the following SQL code:
```
SELECT 
    d.name AS department,
    j.name AS job,
    COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 1 AND 3 THEN 1 END) AS 'Q1',
    COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 4 AND 6 THEN 1 END) AS 'Q2',
    COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 7 AND 9 THEN 1 END) AS 'Q3',
    COUNT(CASE WHEN MONTH(e.date_time) BETWEEN 10 AND 12 THEN 1 END) AS 'Q4'
FROM
    employees e
    INNER JOIN departments d ON e.department_id = d.id
    INNER JOIN jobs j ON e.job_id = j.id
WHERE
    YEAR(e.date_time) = 2021
GROUP BY
    department, job
ORDER BY
    department, job;
```

### Query 2
this query results in the list of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending). To see the result, write in your terminal:
```
curl http://127.0.0.1:5000/sql_query2
```
This query is created with the following SQL code:
```
SELECT
    d.id AS id,
    d.name AS department,
    COUNT(e.id) AS hired
FROM
    departments d
    INNER JOIN employees e ON e.department_id = d.id
WHERE
    YEAR(e.date_time) = 2021
GROUP BY
    id, department
HAVING
    COUNT(e.id) > (
        SELECT AVG(count_emp)
        FROM (
            SELECT COUNT(e.id) AS count_emp
            FROM employees e
            WHERE YEAR(e.date_time) = 2021
            GROUP BY e.department_id
        ) AS sub
    )
ORDER BY
	hired DESC;
```
