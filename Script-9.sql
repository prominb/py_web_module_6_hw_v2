SELECT DISTINCT s2.subject_name, s.last_name  
FROM students s 
JOIN grades g ON g.student_id = s.id 
JOIN subjects s2 ON s2.id = g.subject_id 
WHERE s.id = 38;