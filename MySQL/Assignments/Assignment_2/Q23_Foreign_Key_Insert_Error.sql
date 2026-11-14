-- Q23) Try inserting an Issue record with a Member_Id
-- that does not exist in Member.
-- 999 is intentionally used as an invalid Member_Id.
-- Expected: ERROR 1452 (Foreign Key constraint fails).

INSERT INTO Issue
(Book_No, Member_Id, Issue_Date)
VALUES
(102, 999, '2024-12-25');
