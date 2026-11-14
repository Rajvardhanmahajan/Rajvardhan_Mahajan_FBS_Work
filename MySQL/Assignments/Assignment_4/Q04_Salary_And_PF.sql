-- Q4) Display first_name, last_name, salary and PF.
-- PF is calculated as 15% of salary.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY,
       SALARY * 0.15 AS PF
FROM EMPLOYEES;
