select concat(s.last_name, ' ', s.first_name) as FulL_name, round(avg(g.grade), 2) as avgrade 
from students s 
join grades g on s.id = g.student_id
group by concat(s.last_name, ' ', s.first_name) 
order by avgrade desc 
limit 5;