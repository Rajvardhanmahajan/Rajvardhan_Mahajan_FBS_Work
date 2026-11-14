-- ============================================================
-- MYSQL ASSIGNMENT - 4
-- Complete Queries: Q1 to Q21
-- ============================================================

-- ==================== ALL QUERIES TOGETHER ====================

-- Q1) Display employee first_name and last_name with suitable column aliases.

SELECT FIRST_NAME AS 'FIRST NAME',
       LAST_NAME AS 'LAST NAME'
FROM EMPLOYEES;


-- Q2) Display all different department IDs available in EMPLOYEES.

SELECT DISTINCT DEPARTMENT_ID
FROM EMPLOYEES;


-- Q3) Display all employee details sorted by first_name in descending order.

SELECT *
FROM EMPLOYEES
ORDER BY FIRST_NAME DESC;


-- Q4) Display first_name, last_name, salary and PF.
-- PF is calculated as 15% of salary.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY,
       SALARY * 0.15 AS PF
FROM EMPLOYEES;


-- Q5) Display employee_id, employee names and salary
-- sorted in increasing order of salary.

SELECT EMPLOYEE_ID,
       CONCAT(FIRST_NAME, ' ', LAST_NAME) AS EMPLOYEE_NAME,
       SALARY
FROM EMPLOYEES
ORDER BY SALARY ASC;


-- Q6) Display the total salary payable to all employees.

SELECT SUM(SALARY) AS TOTAL_SALARY
FROM EMPLOYEES;


-- Q7) Display the highest and lowest salary.

SELECT MAX(SALARY) AS HIGHEST_SALARY,
       MIN(SALARY) AS LOWEST_SALARY
FROM EMPLOYEES;


-- Q8) Display average salary and total number of employees.

SELECT AVG(SALARY) AS AVERAGE_SALARY,
       COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEES;


-- Q9) Display the total number of employees working in the company.

SELECT COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEES;


-- Q10) Display the number of different job roles available.

SELECT COUNT(DISTINCT JOB_ID) AS DIFFERENT_JOB_ROLES
FROM EMPLOYEES;


-- Q11) Display the first 10 employee records.

SELECT *
FROM EMPLOYEES
LIMIT 10;


-- Q12) Display employee names and salary where salary is
-- less than 10000 or greater than 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE SALARY < 10000
   OR SALARY > 15000;


-- Q13) Display employee names and department_id for
-- department 30 and department 100.
-- Sort the result by department_id.

SELECT FIRST_NAME,
       LAST_NAME,
       DEPARTMENT_ID
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
ORDER BY DEPARTMENT_ID;


-- Q14) Display employee names and salary for employees
-- in department 30 or 100 whose salary is outside 10000 to 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
  AND SALARY NOT BETWEEN 10000 AND 15000;


-- Q15) Display employee names and hire_date for employees
-- hired in the year 1987.

SELECT FIRST_NAME,
       LAST_NAME,
       HIRE_DATE
FROM EMPLOYEES
WHERE YEAR(HIRE_DATE) = 1987;


-- Q16) Display first_name of employees whose first_name
-- contains both letters 'b' and 'c'.

SELECT FIRST_NAME
FROM EMPLOYEES
WHERE FIRST_NAME LIKE '%b%'
  AND FIRST_NAME LIKE '%c%';


-- Q17) Display last_name, job role and salary for employees
-- who work as Programmer or Shipping Clerk and whose salary
-- is not equal to 4500, 10000 or 15000.
--
-- JOB_ID values below are based on the standard HR JOBS table:
-- IT_PROG = Programmer, SH_CLERK = Shipping Clerk.

SELECT e.LAST_NAME,
       j.JOB_TITLE AS JOB_ROLE,
       e.SALARY
FROM EMPLOYEES e
JOIN JOBS j
  ON e.JOB_ID = j.JOB_ID
WHERE j.JOB_TITLE IN ('Programmer', 'Shipping Clerk')
  AND e.SALARY NOT IN (4500, 10000, 15000);


-- Q18) Display last_name containing exactly 6 characters.

SELECT LAST_NAME
FROM EMPLOYEES
WHERE LAST_NAME LIKE '______';


-- Q19) Display last_name having 'e' as the third character.

SELECT LAST_NAME
FROM EMPLOYEES
WHERE LAST_NAME LIKE '__e%';


-- Q20) Display all different job roles/designations.
-- JOB_TITLE is taken from JOBS.

SELECT DISTINCT j.JOB_TITLE AS JOB_ROLE
FROM EMPLOYEES e
JOIN JOBS j
  ON e.JOB_ID = j.JOB_ID;


-- Q21) Display employee details for employees whose
-- last_name is BLAKE, SCOTT, KING or FORD.

SELECT *
FROM EMPLOYEES
WHERE LAST_NAME IN ('BLAKE', 'SCOTT', 'KING', 'FORD');


-- ============================================================
-- QUESTION-WISE QUERIES
-- ============================================================

-- Q1) Display employee first_name and last_name with suitable column aliases.

SELECT FIRST_NAME AS 'FIRST NAME',
       LAST_NAME AS 'LAST NAME'
FROM EMPLOYEES;


-- Q2) Display all different department IDs available in EMPLOYEES.

SELECT DISTINCT DEPARTMENT_ID
FROM EMPLOYEES;


-- Q3) Display all employee details sorted by first_name in descending order.

SELECT *
FROM EMPLOYEES
ORDER BY FIRST_NAME DESC;


-- Q4) Display first_name, last_name, salary and PF.
-- PF is calculated as 15% of salary.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY,
       SALARY * 0.15 AS PF
FROM EMPLOYEES;


-- Q5) Display employee_id, employee names and salary
-- sorted in increasing order of salary.

SELECT EMPLOYEE_ID,
       CONCAT(FIRST_NAME, ' ', LAST_NAME) AS EMPLOYEE_NAME,
       SALARY
FROM EMPLOYEES
ORDER BY SALARY ASC;


-- Q6) Display the total salary payable to all employees.

SELECT SUM(SALARY) AS TOTAL_SALARY
FROM EMPLOYEES;


-- Q7) Display the highest and lowest salary.

SELECT MAX(SALARY) AS HIGHEST_SALARY,
       MIN(SALARY) AS LOWEST_SALARY
FROM EMPLOYEES;


-- Q8) Display average salary and total number of employees.

SELECT AVG(SALARY) AS AVERAGE_SALARY,
       COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEES;


-- Q9) Display the total number of employees working in the company.

SELECT COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEES;


-- Q10) Display the number of different job roles available.

SELECT COUNT(DISTINCT JOB_ID) AS DIFFERENT_JOB_ROLES
FROM EMPLOYEES;


-- Q11) Display the first 10 employee records.

SELECT *
FROM EMPLOYEES
LIMIT 10;


-- Q12) Display employee names and salary where salary is
-- less than 10000 or greater than 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE SALARY < 10000
   OR SALARY > 15000;


-- Q13) Display employee names and department_id for
-- department 30 and department 100.
-- Sort the result by department_id.

SELECT FIRST_NAME,
       LAST_NAME,
       DEPARTMENT_ID
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
ORDER BY DEPARTMENT_ID;


-- Q14) Display employee names and salary for employees
-- in department 30 or 100 whose salary is outside 10000 to 15000.

SELECT FIRST_NAME,
       LAST_NAME,
       SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (30, 100)
  AND SALARY NOT BETWEEN 10000 AND 15000;


-- Q15) Display employee names and hire_date for employees
-- hired in the year 1987.

SELECT FIRST_NAME,
       LAST_NAME,
       HIRE_DATE
FROM EMPLOYEES
WHERE YEAR(HIRE_DATE) = 1987;


-- Q16) Display first_name of employees whose first_name
-- contains both letters 'b' and 'c'.

SELECT FIRST_NAME
FROM EMPLOYEES
WHERE FIRST_NAME LIKE '%b%'
  AND FIRST_NAME LIKE '%c%';


-- Q17) Display last_name, job role and salary for employees
-- who work as Programmer or Shipping Clerk and whose salary
-- is not equal to 4500, 10000 or 15000.
--
-- JOB_ID values below are based on the standard HR JOBS table:
-- IT_PROG = Programmer, SH_CLERK = Shipping Clerk.

SELECT e.LAST_NAME,
       j.JOB_TITLE AS JOB_ROLE,
       e.SALARY
FROM EMPLOYEES e
JOIN JOBS j
  ON e.JOB_ID = j.JOB_ID
WHERE j.JOB_TITLE IN ('Programmer', 'Shipping Clerk')
  AND e.SALARY NOT IN (4500, 10000, 15000);


-- Q18) Display last_name containing exactly 6 characters.

SELECT LAST_NAME
FROM EMPLOYEES
WHERE LAST_NAME LIKE '______';


-- Q19) Display last_name having 'e' as the third character.

SELECT LAST_NAME
FROM EMPLOYEES
WHERE LAST_NAME LIKE '__e%';


-- Q20) Display all different job roles/designations.
-- JOB_TITLE is taken from JOBS.

SELECT DISTINCT j.JOB_TITLE AS JOB_ROLE
FROM EMPLOYEES e
JOIN JOBS j
  ON e.JOB_ID = j.JOB_ID;


-- Q21) Display employee details for employees whose
-- last_name is BLAKE, SCOTT, KING or FORD.

SELECT *
FROM EMPLOYEES
WHERE LAST_NAME IN ('BLAKE', 'SCOTT', 'KING', 'FORD');
