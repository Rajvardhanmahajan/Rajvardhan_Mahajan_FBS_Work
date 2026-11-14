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
