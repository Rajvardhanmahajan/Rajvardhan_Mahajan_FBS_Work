-- Q14) Display employee names and salary for employees
-- in department 30 or 100 whose salary is outside 10000 to 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
  AND SALARY NOT BETWEEN 10000 AND 15000;
