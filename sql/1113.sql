# Write your MySQL query statement below
SELECT extra AS report_reason, COUNT(DISTINCT post_id) as report_count
FROM Actions
WHERE extra IS NOT NULL AND action = 'report' AND action_date = SUBDATE('2019-07-05', 1)
GROUP BY extra
