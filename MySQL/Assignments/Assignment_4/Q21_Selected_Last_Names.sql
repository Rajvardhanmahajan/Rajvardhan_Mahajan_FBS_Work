-- Q21) Display employee details for employees whose
-- last_name is BLAKE, SCOTT, KING or FORD.

SELECT *
FROM EMPLOYEES
WHERE LAST_NAME IN ('BLAKE', 'SCOTT', 'KING', 'FORD');
