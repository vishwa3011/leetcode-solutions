# Write your MySQL query statement below

with cte as(
select id, email, row_number() over(partition by email order by id) as rn
from person
)

select distinct email
from cte where rn != 1