-- Q25) Update Return_Date for Issue 7004 and 7005
-- to 15 days after Issue_Date.
-- Return_Date already exists in the assignment schema.

UPDATE Issue
SET Return_Date = DATE_ADD(Issue_Date, INTERVAL 15 DAY)
WHERE Lib_Issue_Id IN (7004, 7005);

-- Verify the updated dates.

SELECT Lib_Issue_Id, Issue_Date, Return_Date
FROM Issue
WHERE Lib_Issue_Id IN (7004, 7005);
