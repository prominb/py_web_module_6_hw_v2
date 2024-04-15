SELECT ім'я, AVG(оцінка) AS середній_бал
FROM студенти
GROUP BY ім'я
ORDER BY середній_бал DESC
LIMIT 5;
