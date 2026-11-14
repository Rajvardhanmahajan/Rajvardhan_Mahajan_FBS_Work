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
