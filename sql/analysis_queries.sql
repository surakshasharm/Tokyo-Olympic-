-- Total athletes per team
SELECT Team, COUNT(*) AS total_athletes
FROM athletes
GROUP BY Team
ORDER BY total_athletes DESC;

-- Total medals by country
SELECT Team, SUM(Gold) as gold_medals, SUM(Silver) as silver_medals, SUM(Bronze) as bronze_medals
FROM medals
GROUP BY Team
ORDER BY gold_medals DESC;
