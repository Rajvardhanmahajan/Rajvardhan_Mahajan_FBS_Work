-- ============================================================
-- MYSQL ASSIGNMENT - 2
-- Complete Queries: Q1 to Q28
-- ============================================================
-- Run the questions in order because later questions depend on
-- tables/data created or modified by earlier questions.
-- ============================================================

-- ==================== Q01_Create_Tables ====================

-- Q1) Create Member, Books and Issue tables WITHOUT constraints.
-- Note: Datatypes are taken from the assignment schema.

CREATE TABLE Member (
    Member_Id INT,
    Member_Name VARCHAR(30),
    Member_Address VARCHAR(50),
    Acc_Open_Date DATE,
    Membership_Type VARCHAR(20),
    Fees_Paid DECIMAL(10,2),
    Max_Books_Allowed INT,
    Penalty_Amount DECIMAL(10,2)
);

CREATE TABLE Books (
    Book_No INT,
    Book_Name VARCHAR(30),
    Author_Name VARCHAR(30),
    Cost DECIMAL(10,2),
    Category VARCHAR(15)
);

CREATE TABLE Issue (
    Lib_Issue_Id INT,
    Book_No INT,
    Member_Id INT,
    Issue_Date DATE,
    Return_Date DATE
);

-- ==================== Q02_Display_Table_Structure ====================

-- Q2) Display the structure of all three tables.

DESC Member;
DESC Books;
DESC Issue;

-- ==================== Q03_Drop_Member ====================

-- Q3) Drop the Member table.

DROP TABLE Member;

-- ==================== Q04_Create_Member_With_Constraints ====================

-- Q4) Create Member table again with constraints.
-- Member_Id -> PRIMARY KEY
-- Membership_Type -> only Lifetime, Annual, Half Yearly or Quarterly

CREATE TABLE Member (
    Member_Id INT PRIMARY KEY,
    Member_Name VARCHAR(30),
    Member_Address VARCHAR(50),
    Acc_Open_Date DATE,
    Membership_Type VARCHAR(20)
        CHECK (Membership_Type IN
        ('Lifetime', 'Annual', 'Half Yearly', 'Quarterly')),
    Fees_Paid DECIMAL(10,2),
    Max_Books_Allowed INT,
    Penalty_Amount DECIMAL(10,2)
);

-- ==================== Q05_Increase_Member_Name_Size ====================

-- Q5) Increase Member_Name size from 30 to 40.

ALTER TABLE Member
MODIFY Member_Name VARCHAR(40);

-- ==================== Q06_Add_Reference_Column ====================

-- Q6) Add Reference column to Issue table.

ALTER TABLE Issue
ADD Reference VARCHAR(30);

-- ==================== Q07_Drop_Reference_Column ====================

-- Q7) Drop Reference column from Issue table.

ALTER TABLE Issue
DROP COLUMN Reference;

-- ==================== Q08_Rename_Issue_To_Lib_Issue ====================

-- Q8) Rename Issue table to Lib_Issue.

RENAME TABLE Issue TO Lib_Issue;

-- ==================== Q09_Insert_Member_Records ====================

-- Q9) Insert the given records into Member table.
-- '10-12-05' in the assignment is treated as 2005-12-10.
-- CURRENT_DATE inserts today's date for Garima Sen.

INSERT INTO Member
(Member_Id, Member_Name, Member_Address, Acc_Open_Date,
 Membership_Type, Fees_Paid, Max_Books_Allowed, Penalty_Amount)
VALUES
(1, 'Richa Sharma', 'Pune', '2005-12-10',
 'Lifetime', 25000.00, 5, 50.00),
(2, 'Garima Sen', 'Pune', CURRENT_DATE,
 'Annual', 1000.00, 3, NULL);

-- ==================== Q10_Insert_5_More_Members ====================

-- Q10) Insert at least 5 more suitable records into Member table.

INSERT INTO Member
(Member_Id, Member_Name, Member_Address, Acc_Open_Date,
 Membership_Type, Fees_Paid, Max_Books_Allowed, Penalty_Amount)
VALUES
(3, 'Rahul Patil', 'Mumbai', '2025-01-15',
 'Annual', 10000.00, 3, 0.00),
(4, 'Sneha Desai', 'Nashik', '2025-02-20',
 'Quarterly', 3000.00, 2, 100.00),
(5, 'Amit Sharma', 'Pune', '2025-03-10',
 'Half Yearly', 6000.00, 4, 50.00),
(6, 'Priya Joshi', 'Nagpur', '2025-04-05',
 'Lifetime', 25000.00, 5, 0.00),
(7, 'Vikas More', 'Kolhapur', '2025-05-12',
 'Annual', 10000.00, 3, 150.00);

-- ==================== Q11_Decrease_Member_Name_Size ====================

-- Q11) Try to decrease Member_Name size from 40 to 20.
-- If the modification fails, record the MySQL error/reason.
-- This statement is valid if all existing names fit within 20 characters.

ALTER TABLE Member
MODIFY Member_Name VARCHAR(20);

-- ==================== Q12_Add_Check_Constraint ====================

-- Q12) Add CHECK constraint:
-- Max_Books_Allowed must be less than 100.

ALTER TABLE Member
ADD CONSTRAINT chk_max_books_q12
CHECK (Max_Books_Allowed < 100);

-- ==================== Q13_Create_Member_Backup ====================

-- Q13) Create a backup table using the Member table.
-- CREATE TABLE ... AS SELECT copies the current data and column structure,
-- but it does not copy the original table's constraints.

CREATE TABLE MemberBackup AS
SELECT * FROM Member;

-- ==================== Q14_Add_Named_Check_Constraints ====================

-- Q14) Add named CHECK constraints.
-- Important: Q12 already added the same logical condition.
-- If Q12 was executed successfully, do NOT add the duplicate Max_Books
-- condition again. The second statement can be executed independently.

-- Named version of Max_Books_Allowed < 100:
-- Run this only if the Q12 constraint has been removed/not created.
-- ALTER TABLE Member
-- ADD CONSTRAINT chk_max_books
-- CHECK (Max_Books_Allowed < 100);

-- Named constraint for Penalty_Amount <= 1000:
ALTER TABLE Member
ADD CONSTRAINT chk_penalty_amount
CHECK (Penalty_Amount <= 1000);

-- ==================== Q15_Drop_Books ====================

-- Q15) Drop the Books table.

DROP TABLE Books;

-- ==================== Q16_Create_Books_With_Constraints ====================

-- Q16) Create Books table again with constraints.
-- Book_No -> PRIMARY KEY
-- Book_Name -> NOT NULL
-- Category -> restricted to the specified values.

CREATE TABLE Books (
    Book_No INT PRIMARY KEY,
    Book_Name VARCHAR(30) NOT NULL,
    Author_Name VARCHAR(30) NOT NULL,
    Cost DECIMAL(10,2),
    Category VARCHAR(15)
        CHECK (Category IN
        ('System', 'Fiction', 'Database', 'RDBMS', 'Others', 'Science'))
);

-- ==================== Q17_Insert_Books ====================

-- Q17) Insert the given records into Books table.

INSERT INTO Books
(Book_No, Book_Name, Author_Name, Cost, Category)
VALUES
(101, 'Let Us C', 'Denis Ritchie', 450.00, 'System'),
(102, 'Oracle Complete Ref', 'Loni', 550.00, 'Database'),
(103, 'Mastering SQL', 'Loni', 250.00, 'Database'),
(104, 'PL SQL Ref', 'Scott Urman', 750.00, 'Database'),
(105, 'National Geographic', 'Adis Scott', 1000.00, 'Science');

-- ==================== Q18_Insert_5_More_Books ====================

-- Q18) Insert at least 5 more suitable records into Books table.

INSERT INTO Books
(Book_No, Book_Name, Author_Name, Cost, Category)
VALUES
(106, 'Java Basics', 'Herbert Schildt', 600.00, 'System'),
(107, 'SQL Fundamentals', 'John Smith', 500.00, 'RDBMS'),
(108, 'The Alchemist', 'Paulo Coelho', 350.00, 'Fiction'),
(109, 'Python Guide', 'Mark Lutz', 700.00, 'Others'),
(110, 'Data Science Basics', 'John Doe', 800.00, 'Science');

-- ==================== Q19_View_Member_And_Books ====================

-- Q19) View all data from Member and Books tables.

SELECT * FROM Member;

SELECT * FROM Books;

-- ==================== Q20_Drop_Lib_Issue ====================

-- Q20) Drop the Lib_Issue table.

DROP TABLE Lib_Issue;

-- ==================== Q21_Create_Issue_With_Foreign_Keys ====================

-- Q21) Create Issue table again with constraints.
-- Lib_Issue_Id -> PRIMARY KEY
-- Book_No -> FOREIGN KEY referencing Books(Book_No)
-- Member_Id -> FOREIGN KEY referencing Member(Member_Id)

CREATE TABLE Issue (
    Lib_Issue_Id INT PRIMARY KEY,
    Book_No INT,
    Member_Id INT,
    Issue_Date DATE,
    Return_Date DATE,
    FOREIGN KEY (Book_No) REFERENCES Books(Book_No),
    FOREIGN KEY (Member_Id) REFERENCES Member(Member_Id)
);

-- ==================== Q22_Insert_Issue_Records ====================

-- Q22) Insert the given records into Issue table.

INSERT INTO Issue
(Lib_Issue_Id, Book_No, Member_Id, Issue_Date)
VALUES
(7001, 101, 1, '2024-12-10'),
(7002, 102, 2, '2024-12-25'),
(7003, 104, 1, '2025-01-15'),
(7004, 101, 1, '2025-02-04'),
(7005, 104, 2, '2025-03-15'),
(7006, 101, 3, '2025-04-18');

-- ==================== Q23_Foreign_Key_Insert_Error ====================

-- Q23) Try inserting an Issue record with a Member_Id
-- that does not exist in Member.
-- 999 is intentionally used as an invalid Member_Id.
-- Expected: ERROR 1452 (Foreign Key constraint fails).

INSERT INTO Issue
(Book_No, Member_Id, Issue_Date)
VALUES
(102, 999, '2024-12-25');

-- ==================== Q24_Foreign_Key_Delete_Error ====================

-- Q24) Try deleting Member_Id = 1.
-- Member_Id = 1 is referenced by Issue, so MySQL should reject
-- the deletion with ERROR 1451.
-- Expected: Cannot delete or update a parent row.

DELETE FROM Member
WHERE Member_Id = 1;

-- ==================== Q25_Update_Return_Date ====================

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

-- ==================== Q26_Delete_Old_Issues ====================

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

-- ==================== Q27_Delete_Non_Database_RDBMS_Books ====================

-- Q27) Delete all Books whose Category is not Database or RDBMS.
-- NOTE: If a Book_No is already referenced by Issue, MySQL will raise
-- ERROR 1451 because of the Foreign Key constraint.

DELETE FROM Books
WHERE Category NOT IN ('Database', 'RDBMS');

-- ==================== Q28_Drop_All_Tables ====================

-- Q28) Drop all three tables.
-- Because Issue contains Foreign Keys to Member and Books,
-- drop Issue first, then Member and Books.

DROP TABLE Issue;
DROP TABLE Member;
DROP TABLE Books;