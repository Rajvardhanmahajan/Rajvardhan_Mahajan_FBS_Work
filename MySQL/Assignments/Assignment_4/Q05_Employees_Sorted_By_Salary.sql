-- Q5) Display employee_id, employee names and salary
-- sorted in increasing order of salary.

SELECT EMPLOYEE_ID,
       CONCAT(FIRST_NAME, ' ', LAST_NAME) AS EMPLOYEE_NAME,
       SALARY
FROM EMPLOYEES
ORDER BY SALARY ASC;
