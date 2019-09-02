# # Write your MySQL query statement below
select p.project_id, p.employee_id from Project p inner join
(select project_id, max(experience_years) as experience_years
from Project p inner join Employee e on p.employee_id = e.employee_id
group by project_id) x
on p.project_id = x.project_id
inner join Employee e on
p.employee_id = e.employee_id and e.experience_years = x.experience_years
