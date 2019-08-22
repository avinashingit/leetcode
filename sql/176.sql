# Write your MySQL query statement below
select Salary as SecondHighestSalary from Employee where Salary
not in (select max(Salary) from Employee) order by Salary desc Limit 1

select ifnull((select Distinct Salary as sal from Employee order by sal desc limit 1 offset 1), NULL)
as SecondHighestSalary
