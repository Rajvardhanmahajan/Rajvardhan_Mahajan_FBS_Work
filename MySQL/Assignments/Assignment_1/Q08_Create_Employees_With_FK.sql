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
