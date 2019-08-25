# Write your MySQL query statement below
SELECT w2.Id as Id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w2.RecordDate, w1.RecordDate) = 1 AND w2.Temperature > w1.Temperature
