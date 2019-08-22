select project_id
from Project inner join Employee on Project.employee_id = Employee.employee_id
group by Project.project_id
having count(Employee.employee_id) = (select max(emp_count) from (select count(distinct Employee.employee_id) as emp_count
from Project inner join Employee on Project.employee_id = Employee.employee_id
group by Project.project_id) t1)
