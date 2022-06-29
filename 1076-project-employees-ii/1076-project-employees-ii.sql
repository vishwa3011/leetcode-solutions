# Write your MySQL query statement below
with cte
as (
Select project_id, count(employee_id) as cnt
from Project
group by project_id
)

Select project_id from cte
where cnt = (Select max(cnt) from cte)