-- script that displays the max temperature of each state
SELECT state, max(value) AS max_temp FROM temperatures ORDER BY state;
