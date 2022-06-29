# Write your MySQL query statement below
with cte
as (
Select project_id, count(employee_id) as cnt
from Project
group by project_id
)

Select project_id from cte
where cnt = (Select max(cnt) from cte)

# select project_id
# from Project
# group by project_id
# having count(employee_id) = (
#     select max(empcount) from
#     (
# select count(employee_id) as empcount
# from Project
# group by project_id) xx)