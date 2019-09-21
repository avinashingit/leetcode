SELECT Request_at as Day,
ROUND(SUM(CASE WHEN Status = 'completed' THEN 0 ELSE 1 end)/count(Id),2) AS 'Cancellation Rate'
FROM Trips T
WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND
Client_Id in (
SELECT U1.Users_Id FROM Users U1 WHERE Banned = 'No'
)
AND
Driver_Id in (
SELECT U1.Users_Id FROM Users U1 WHERE Banned = 'No'
)
GROUP BY Request_at
