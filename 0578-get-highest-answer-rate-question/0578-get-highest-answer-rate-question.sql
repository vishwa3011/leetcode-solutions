# Write your MySQL query statement below

with answer_rate_cte
as
(
select question_id, sum(case when action = 'answer' then 1 else 0 end)/sum(case when action = 'show' then 1 else 0 end) as answer_rate
    from surveylog
    group by question_id
)
select question_id as survey_log
from answer_rate_cte
order by answer_rate desc, question_id
limit 1;