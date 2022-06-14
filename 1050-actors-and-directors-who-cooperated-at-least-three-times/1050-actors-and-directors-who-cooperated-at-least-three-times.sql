# Write your MySQL query statement below

with cte as
(
Select actor_id, director_id, count(*) as cnt
from ActorDirector
group by actor_id, director_id
)

select actor_id, director_id
from cte where cnt >= 3

