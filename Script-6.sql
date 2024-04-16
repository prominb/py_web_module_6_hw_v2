SELECT concat(s.last_name, ' ', s.first_name) AS fullname 
FROM "groups" g 
JOIN students s ON s.group_id = g.id 
WHERE g.id = 2
--WHERE g.group_name LIKE '%23%' 
ORDER BY s.last_name;