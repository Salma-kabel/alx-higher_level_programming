-- script that displays the average temperature (Fahrenheit) by city
SELECT city, AVG(value) as avg_temp FROM temperatures ORDER BY avg_temp;
