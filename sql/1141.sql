# Write your MySQL query statement below
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN SUBDATE('2019-07-27', 29) AND '2019-07-27'
GROUP BY activity_date
