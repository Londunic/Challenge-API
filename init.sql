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