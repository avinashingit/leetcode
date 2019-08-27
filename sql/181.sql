# Write your MySQL query statement below
select t.Name as Employee from (
select e1.Name as name, case when e1.Salary > e2.Salary then 1 else 0 end as more_salary
from Employee e1 inner join Employee e2 on e1.ManagerId = e2.Id) t
where t.more_salary = 1
