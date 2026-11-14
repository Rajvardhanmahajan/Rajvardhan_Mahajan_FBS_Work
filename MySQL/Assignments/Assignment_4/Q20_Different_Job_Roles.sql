-- Q20) Display all different job roles/designations.
-- JOB_TITLE is taken from JOBS.

SELECT DISTINCT j.JOB_TITLE AS JOB_ROLE
FROM EMPLOYEES e
JOIN JOBS j
  ON e.JOB_ID = j.JOB_ID;
