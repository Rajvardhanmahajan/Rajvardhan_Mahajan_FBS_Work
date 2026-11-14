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
