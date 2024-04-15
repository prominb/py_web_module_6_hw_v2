select g2.group_name, round(avg(g.grade), 2) as avg_grade
from grades g 
join subjects s on s.id = g.subject_id 
join students s2 on s2.id = g.student_id 
join "groups" g2 on g2.id = s2.group_id 
where s.id = 6
group by g2.group_name
--order by avg_grade desc
order by g2.group_name 
;