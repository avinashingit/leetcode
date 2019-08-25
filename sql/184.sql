# Write your MySQL query statement below

SELECT Dep.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
FROM Employee INNER JOIN
(SELECT DepartmentId, Department.Name, MAX(Salary) as Salary
FROM Employee INNER JOIN Department ON Employee.DepartmentId = Department.Id
GROUP BY DepartmentId) Dep
ON Employee.DepartmentId = Dep.DepartmentId AND Employee.Salary = Dep.Salary
