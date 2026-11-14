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
