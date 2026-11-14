-- Q26) Delete Issue records where:
-- Member_Id = 1 AND Issue_Date is before 2006-12-10.

DELETE FROM Issue
WHERE Member_Id = 1
AND Issue_Date < '2006-12-10';

-- Verify if any matching records remain.

SELECT *
FROM Issue
WHERE Member_Id = 1
AND Issue_Date < '2006-12-10';
