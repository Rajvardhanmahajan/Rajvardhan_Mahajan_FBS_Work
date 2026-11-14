-- Q3) Insert one new job record.
-- JOB_ID is PRIMARY KEY, so duplicate JOB_ID values are not allowed.

INSERT INTO JOBS
(JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY)
VALUES
(20, 'Data Analyst', 30000.00, 70000.00);
