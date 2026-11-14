-- Q13) Display employee names and department_id for
-- department 30 and department 100.
-- Sort the result by department_id.

SELECT FIRST_NAME,
       LAST_NAME,
       DEPARTMENT_ID
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
ORDER BY DEPARTMENT_ID;
