-- Q5) Add UNIQUE Constraint
-- Prevent duplicate country_id values in the countries table.

ALTER TABLE countries
ADD CONSTRAINT uq_country_id UNIQUE (country_id);
