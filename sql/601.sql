# Write your MySQL query statement below
SELECT  distinct t1.*
FROM stadium t1, stadium t2, stadium t3
WHERE t1.people >= 100 and t2.people >= 100 and t3.people >= 100 AND
((t2.id-t1.id = 1 AND t3.id-t1.id = 2 and t3.id - t2.id = 1) OR
(t1.id-t2.id = 1 AND t3.id-t2.id = 2 and t3.id-t1.id = 1) OR
(t2.id-t3.id = 1 AND t1.id-t3.id = 2 and t1.id-t2.id = 1))
order by t1.id
