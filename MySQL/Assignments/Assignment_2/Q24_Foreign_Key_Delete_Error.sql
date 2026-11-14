-- Q24) Try deleting Member_Id = 1.
-- Member_Id = 1 is referenced by Issue, so MySQL should reject
-- the deletion with ERROR 1451.
-- Expected: Cannot delete or update a parent row.

DELETE FROM Member
WHERE Member_Id = 1;
