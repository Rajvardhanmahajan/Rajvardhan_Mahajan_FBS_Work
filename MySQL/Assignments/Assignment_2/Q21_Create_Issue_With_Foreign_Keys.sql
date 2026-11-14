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
