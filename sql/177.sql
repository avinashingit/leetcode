CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare M INT;
If N = 0 Then SET M = 0;
else SET M = N-1;
END IF;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary from Employee
      order by Salary desc
      limit 1 offset M
  );
END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT
        CASE WHEN (SELECT COUNT(DISTINCT Salary) FROM Employee) < N THEN NULL
        ELSE (SELECT min(s.Salary) FROM (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N) as s)
      END
  );
END
