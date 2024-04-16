SELECT
	concat(t.first_name, ' ', t.last_name) AS fullname,
	s.subject_name
FROM subjects s
JOIN teachers t ON t.id = s.teacher_id
WHERE t.id = 1;
--WHERE t.last_name LIKE 'Баб%';