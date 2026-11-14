-- Q12) Add CHECK constraint:
-- Max_Books_Allowed must be less than 100.

ALTER TABLE Member
ADD CONSTRAINT chk_max_books_q12
CHECK (Max_Books_Allowed < 100);
