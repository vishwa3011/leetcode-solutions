# Write your MySQL query statement below


# Total unbanned requests

with total_unbanned as
(
select t.request_at, count(*) as total_requests
from trips t join users c on t.client_id = c.users_id
    join users d on t.driver_id = d.users_id
    where c.banned = 'No' and d.banned = 'No'
group by t.request_at
),

# Total cancelled requests
cancelled_unbanned as
(
select t.request_at, sum(t.Status != "completed") as cancelled_requests
from trips t join users c on t.client_id = c.users_id
    join users d on t.driver_id = d.users_id
where c.banned = 'No' and d.banned = 'No'
group by t.request_at
)

#select * from tot_unbanned
select t.request_at as Day, round(c.cancelled_requests/t.total_requests, 2) as 'Cancellation Rate'
from total_unbanned t join cancelled_unbanned c
on t.request_at = c.request_at
where t.request_at BETWEEN '2013-10-01' and '2013-10-03'
group by t.request_at