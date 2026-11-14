-- ============================================================
-- MYSQL ASSIGNMENT - 3
-- Complete Queries Covered So Far: Q1 to Q12
-- ============================================================


-- ==================== Q01_Insert_Employees ====================

-- Q1) Insert the reference employee records into EMPLOYEES.
-- Use the employee data provided in Assignment 3.
--
-- Insert the exact reference records from the assignment PDF here.

-- ==================== Q02_Insert_Departments ====================

-- Q2) Insert at least 3 department records using a single INSERT statement.

INSERT INTO DEPARTMENTS
(DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID, LOCATION_ID)
VALUES
(10, 'Administration', 200, 1700),
(20, 'Marketing', 201, 1800),
(30, 'Purchasing', 114, 1700);

-- ==================== Q03_Insert_Job ====================

-- Q3) Insert one new job record.
-- JOB_ID is PRIMARY KEY, so duplicate JOB_ID values are not allowed.

INSERT INTO JOBS
(JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY)
VALUES
(20, 'Data Analyst', 30000.00, 70000.00);

-- ==================== Q04_Increase_Salary_10_Percent ====================

-- Q4) Increment the salary of each employee by 10%.

UPDATE EMPLOYEES
SET SALARY = SALARY * 1.10;

-- ==================== Q05_Update_Email_Department_80 ====================

-- Q5) Set EMAIL = 'not available'
-- for employees whose department_id is 80
-- and commission_pct is less than 0.20.

UPDATE EMPLOYEES
SET EMAIL = 'not available'
WHERE DEPARTMENT_ID = 80
AND COMMISSION_PCT < 0.20;

-- ==================== Q06_Update_Email_Purchasing ====================

-- Q6) Set EMAIL = 'not available'
-- for employees who belong to the Purchasing department.

UPDATE EMPLOYEES AS e
JOIN DEPARTMENTS AS d
ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
SET e.EMAIL = 'not available'
WHERE d.DEPARTMENT_NAME = 'Purchasing';

-- ==================== Q07_Update_Email_And_Commission ====================

-- Q7) Set EMAIL = 'not available'
-- and COMMISSION_PCT = 0.10 for all employees.

UPDATE EMPLOYEES
SET EMAIL = 'not available',
    COMMISSION_PCT = 0.10;

-- ==================== Q08_Increase_Salary_Department_60 ====================

-- Q8) Increase salary by 2000 for employees
-- working in department_id = 60.

UPDATE EMPLOYEES
SET SALARY = SALARY + 2000
WHERE DEPARTMENT_ID = 60;

-- ==================== Q09_Delete_Low_Salary_Employees ====================

-- Q9) Delete employees whose salary is less than 5000.

DELETE FROM EMPLOYEES
WHERE SALARY < 5000;

-- ==================== Q10_Insert_New_Employee ====================

-- Q10) Insert one new employee record with suitable details.
-- Use a new employee_id.

INSERT INTO EMPLOYEES
(EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_ID, SALARY,
 MANAGER_ID, DEPARTMENT_ID, EMAIL, COMMISSION_PCT)
VALUES
(110, 'Raj', 'Mahajan', 3, 45000.00,
 101, 60, 'raj@example.com', 0.10);

-- ==================== Q11_Update_Manager_Department_80 ====================

-- Q11) Change manager_id to 300
-- for all employees in department_id = 80.

UPDATE EMPLOYEES
SET MANAGER_ID = 300
WHERE DEPARTMENT_ID = 80;

-- ==================== Q12_Delete_Department_20_FK_Error ====================

-- Q12) Delete the department record where department_id = 20.
-- If employees exist in department 20 and a Foreign Key is present,
-- MySQL is expected to return ERROR 1451.

DELETE FROM DEPARTMENTS
WHERE DEPARTMENT_ID = 20;
