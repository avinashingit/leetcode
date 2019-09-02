# Write your MySQL query statement below
select round(avg(x.total_removed/x.total_reported)*100,2) as average_daily_percent from(
select a.action_date, count(distinct case when r.post_id is not null then a.post_id else null end) as total_removed, count(distinct a.post_id) as total_reported
from Actions a LEFT JOIN Removals r ON a.post_id = r.post_id
where a.extra = 'spam'
group by a.action_date
having total_reported > 0) as x
