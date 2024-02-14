-- Displays all records from the 'second_table' where the name is not NULL, ordered by the 'score' column.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
