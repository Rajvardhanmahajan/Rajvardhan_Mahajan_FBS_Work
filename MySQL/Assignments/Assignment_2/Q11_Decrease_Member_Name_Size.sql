-- Q11) Try to decrease Member_Name size from 40 to 20.
-- If the modification fails, record the MySQL error/reason.
-- This statement is valid if all existing names fit within 20 characters.

ALTER TABLE Member
MODIFY Member_Name VARCHAR(20);
