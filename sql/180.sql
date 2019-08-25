# Write your MySQL query statement below
SELECT DISTINCT a.Num as ConsecutiveNums
FROM Logs a, Logs b, Logs c
WHERE a.Id + 1 = b.Id and a.Id + 2 = c.Id and a.Num = b.Num and a.Num = c.Num
