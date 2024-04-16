--ОДНА СЕЕРДНЯ ОЦІНКА з усіх предметів викладача
SELECT t.last_name, round(avg(g.grade),2) AS avg_grade
FROM grades g 
JOIN subjects s ON s.id = g.subject_id 
JOIN teachers t ON t.id = s.teacher_id 
WHERE t.id = 1
GROUP BY t.last_name;

--АБО СЕРЕДНЯ по кожному Предмету
/*SELECT s.subject_name, round(avg(g.grade),2) AS avg_grade 
FROM grades g 
JOIN subjects s ON s.id = g.subject_id 
JOIN teachers t ON t.id = s.teacher_id 
WHERE t.id = 1
GROUP BY s.subject_name;*/