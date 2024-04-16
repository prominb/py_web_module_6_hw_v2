SELECT g2.group_name, concat(s2.last_name, ' ', s2.first_name) AS stud_name, s.subject_name, g.grade, g.grade_date 
FROM grades g 
JOIN subjects s ON g.subject_id = s.id 
JOIN students s2 ON s2.id = g.student_id 
JOIN "groups" g2 ON g2.id = s2.group_id 
WHERE s.id = 1 AND g2.id = 1
ORDER BY s2.last_name ;