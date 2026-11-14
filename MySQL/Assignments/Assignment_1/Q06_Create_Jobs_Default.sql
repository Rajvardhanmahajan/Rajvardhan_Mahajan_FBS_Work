-- Q6) Create jobs_default Table with DEFAULT Values
-- Create the table with the specified default values.

CREATE TABLE jobs_default (
    job_id INT,
    job_title VARCHAR(100) DEFAULT '',
    min_salary DECIMAL(10,2) DEFAULT 8000,
    max_salary DECIMAL(10,2) DEFAULT NULL
);
