-- Q16) Display first_name of employees whose first_name
-- contains both letters 'b' and 'c'.

SELECT FIRST_NAME
FROM EMPLOYEES
WHERE FIRST_NAME LIKE '%b%'
  AND FIRST_NAME LIKE '%c%';
