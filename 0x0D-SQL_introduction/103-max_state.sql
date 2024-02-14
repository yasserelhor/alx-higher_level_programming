-- Displays the average temperature by city for the months of July and August in descending order.
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
