-- Q15) Display employee names and hire_date for employees
-- hired in the year 1987.

SELECT FIRST_NAME,
       LAST_NAME,
       HIRE_DATE
FROM EMPLOYEES
WHERE YEAR(HIRE_DATE) = 1987;
