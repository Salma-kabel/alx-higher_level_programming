-- script that displays the average temperature (Fahrenheit) by city
SELECT city, AVG(value) AS avg_temp FROM temperatures ORDER BY avg_temp;
