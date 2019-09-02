# Write your MySQL query statement below
select round(ifnull(avg(num), 0),2) as average_sessions_per_user from(
select user_id, count(distinct session_id) as num
from Activity
where activity_date <= '2019-07-27' and activity_date > SUBDATE('2019-07-27', 30)
group by user_id) as x
