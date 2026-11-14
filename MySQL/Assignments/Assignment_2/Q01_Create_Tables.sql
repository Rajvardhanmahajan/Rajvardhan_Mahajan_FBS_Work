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
