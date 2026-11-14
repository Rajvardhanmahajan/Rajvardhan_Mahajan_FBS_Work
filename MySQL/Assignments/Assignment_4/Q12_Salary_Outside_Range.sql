-- Q12) Display employee names and salary where salary is
-- less than 10000 or greater than 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE SALARY < 10000
   OR SALARY > 15000;
