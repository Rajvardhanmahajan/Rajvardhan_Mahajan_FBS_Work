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
