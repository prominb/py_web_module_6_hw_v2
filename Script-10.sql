SELECT DISTINCT s.subject_name 
FROM subjects s 
JOIN teachers t ON t.id = s.teacher_id 
JOIN grades g ON g.subject_id = s.id 
JOIN students s2 ON s2.id = g.student_id 
WHERE s2.id = 18 AND t.id = 5;