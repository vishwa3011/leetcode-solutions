# Write your MySQL query statement below

with cte
as
(
Select requester_id as person, count(requester_id) as n_friends
from RequestAccepted
group by requester_id
union all
Select accepter_id as person, count(accepter_id) as n_friends
from RequestAccepted
group by accepter_id
),
cte2
as
(
select person, sum(n_friends) as sum_friends 
from cte
group by person
)

select person as id, sum_friends as num 
from cte2
where sum_friends = (select max(sum_friends) from cte2)