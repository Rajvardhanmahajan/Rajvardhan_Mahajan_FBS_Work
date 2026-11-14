-- Q5) Set EMAIL = 'not available'
-- for employees whose department_id is 80
-- and commission_pct is less than 0.20.

UPDATE EMPLOYEES
SET EMAIL = 'not available'
WHERE DEPARTMENT_ID = 80
AND COMMISSION_PCT < 0.20;
