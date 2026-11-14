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
