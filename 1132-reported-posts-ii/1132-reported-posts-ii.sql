# Write your MySQL query statement below


with percent_cte
as
(
select (count(distinct r.post_id)/count(distinct a.post_id))*100 as percent
from Actions a left join Removals r
on a.post_id = r.post_id
where extra = 'spam'
group by action_date
)

select round(avg(percent),2) as average_daily_percent
from percent_cte