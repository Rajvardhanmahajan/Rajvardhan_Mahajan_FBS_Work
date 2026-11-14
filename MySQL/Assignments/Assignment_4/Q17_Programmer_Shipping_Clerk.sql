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
