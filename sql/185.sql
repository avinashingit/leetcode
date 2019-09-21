# Write your MySQL query statement below
SELECT Department.Name as Department, e1.Name as Employee, e1.Salary as Salary
FROM Employee e1 INNER JOIN Department ON e1.DepartmentId = Department.ID
WHERE 3 > (SELECT COUNT(DISTINCT(e2.Salary)) FROM Employee e2 WHERE e1.Salary < e2.Salary AND e1.DepartmentId = e2.DepartmentId)
