-- Q12) Delete the department record where department_id = 20.
-- If employees exist in department 20 and a Foreign Key is present,
-- MySQL is expected to return ERROR 1451.

DELETE FROM DEPARTMENTS
WHERE DEPARTMENT_ID = 20;
