-- Q6) Set EMAIL = 'not available'
-- for employees who belong to the Purchasing department.

UPDATE EMPLOYEES AS e
JOIN DEPARTMENTS AS d
ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
SET e.EMAIL = 'not available'
WHERE d.DEPARTMENT_NAME = 'Purchasing';
