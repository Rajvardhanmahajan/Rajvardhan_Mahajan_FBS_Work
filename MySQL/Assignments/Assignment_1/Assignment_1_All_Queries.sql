-- Q1) Display Databases
-- Display all databases available in MySQL.

SHOW DATABASES;

-- Q2) Create countries Table
-- Create the countries table and display its structure.

CREATE TABLE countries (
    country_id INT,
    country_name VARCHAR(50),
    region_id INT
);

-- Display the structure of the countries table.
DESC countries;

-- Q3) Create jobs Table with Constraints
-- Create the jobs table with Primary Key, NOT NULL,
-- and CHECK constraint on max_salary.

CREATE TABLE jobs (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(100) NOT NULL,
    min_salary DECIMAL(10,2),
    max_salary DECIMAL(10,2),
    CONSTRAINT chk_max_salary CHECK (max_salary <= 25000)
);

-- Q4) Create job_history Table
-- Create the job_history table.

CREATE TABLE job_history (
    employee_id INT,
    start_date DATE,
    end_date DATE,
    job_id INT,
    department_id INT
);

-- Q5) Add UNIQUE Constraint
-- Prevent duplicate country_id values in the countries table.

ALTER TABLE countries
ADD CONSTRAINT uq_country_id UNIQUE (country_id);

-- Q6) Create jobs_default Table with DEFAULT Values
-- Create the table with the specified default values.

CREATE TABLE jobs_default (
    job_id INT,
    job_title VARCHAR(100) DEFAULT '',
    min_salary DECIMAL(10,2) DEFAULT 8000,
    max_salary DECIMAL(10,2) DEFAULT NULL
);

-- Q7) Create departments Table with Composite Primary Key
-- Create the departments table using department_id and manager_id
-- as a Composite Primary Key.

CREATE TABLE departments (
    department_id DECIMAL(4,0) NOT NULL,
    department_name VARCHAR(30) NOT NULL,
    manager_id DECIMAL(6,0) NOT NULL,
    location_id DECIMAL(4,0),
    PRIMARY KEY (department_id, manager_id)
);

-- Make department_id unique so it can be referenced individually
-- by the normal Foreign Key required in Q8.
ALTER TABLE departments
ADD CONSTRAINT uq_department_id UNIQUE (department_id);

-- Q8) Create employees Table with Normal Foreign Key
-- Create the employees table and make department_id a Foreign Key
-- referencing departments(department_id).

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    hire_date DATE,
    job_id INT,
    salary DECIMAL(10,2),
    commission DECIMAL(10,2),
    manager_id INT,
    department_id INT,
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- Q9) Composite Foreign Key Implementation
-- Step 1: Create department_managers table with a Composite Primary Key.
-- Step 2: Add a Composite Foreign Key in employees table so that
-- (department_id, manager_id) must exist in department_managers.

-- Step 1: Create department_managers Table
CREATE TABLE department_managers (
    department_id DECIMAL(4,0) NOT NULL,
    manager_id DECIMAL(6,0) NOT NULL,
    manager_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (department_id, manager_id)
);

-- Step 2: Apply Composite Foreign Key in employees Table
ALTER TABLE employees
ADD CONSTRAINT fk_employee_manager
FOREIGN KEY (department_id, manager_id)
REFERENCES department_managers(department_id, manager_id);
