-- Q13) Create a backup table using the Member table.
-- CREATE TABLE ... AS SELECT copies the current data and column structure,
-- but it does not copy the original table's constraints.

CREATE TABLE MemberBackup AS
SELECT * FROM Member;
