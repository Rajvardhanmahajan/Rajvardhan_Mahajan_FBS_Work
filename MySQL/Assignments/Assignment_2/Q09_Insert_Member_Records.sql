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
