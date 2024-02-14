-- Lists all records from the 'second_table' sorted in ascending order by the 'score' column.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
