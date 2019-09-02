# Write your MySQL query statement below
select question_id as survey_log from (
    select question_id, sum(case when action='answer' then 1 else 0 end) as total_answers,
    sum(case when action='show' then 1 else 0 end) as total_shows
    from survey_log
    group by question_id) x
order by x.total_answers/(x.total_answers+total_shows) desc
limit 1
