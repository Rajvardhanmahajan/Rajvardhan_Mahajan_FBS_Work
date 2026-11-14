-- Q28) Drop all three tables.
-- Because Issue contains Foreign Keys to Member and Books,
-- drop Issue first, then Member and Books.

DROP TABLE Issue;
DROP TABLE Member;
DROP TABLE Books;
