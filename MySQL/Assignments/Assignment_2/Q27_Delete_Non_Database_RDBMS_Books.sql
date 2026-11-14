-- Q27) Delete all Books whose Category is not Database or RDBMS.
-- NOTE: If a Book_No is already referenced by Issue, MySQL will raise
-- ERROR 1451 because of the Foreign Key constraint.

DELETE FROM Books
WHERE Category NOT IN ('Database', 'RDBMS');
