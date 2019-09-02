# Write your MySQL query statement below
select round(
    ifnull((select count(*) as accept_count from (select distinct requester_id, accepter_id from request_accepted) y)/ (select count(*) as request_count from (select distinct sender_id, send_to_id from friend_request) as A), 0), 2) as accept_rate
