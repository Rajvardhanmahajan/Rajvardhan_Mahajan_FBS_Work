-- Q10) Insert one new employee record with suitable details.
-- Use a new employee_id.

INSERT INTO EMPLOYEES
(EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_ID, SALARY,
 MANAGER_ID, DEPARTMENT_ID, EMAIL, COMMISSION_PCT)
VALUES
(110, 'Raj', 'Mahajan', 3, 45000.00,
 101, 60, 'raj@example.com', 0.10);
