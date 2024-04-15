select concat(s.last_name, ' ', s.first_name) as fulL_name, round(avg(g.grade), 2) as avgrade 
from students s 
join grades g on s.id = g.student_id
join subjects s2 on s2.id = g.subject_id 
where s2.id = 2
group by concat(s.last_name, ' ', s.first_name) 
order by avgrade desc 
limit 1;