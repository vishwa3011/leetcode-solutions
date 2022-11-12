# Write your MySQL query statement below

with answer_cte
as
(
select question_id, sum(case when action = 'answer' then 1 else 0 end) as answer_cnt
    from surveylog
    group by question_id
),
show_cte
as
(
select question_id, sum(case when action = 'show' then 1 else 0 end) as show_cnt
    from surveylog
    group by question_id
),
answer_rate_cte
as
(
select a.question_id, answer_cnt/b.show_cnt as answer_rate
    from answer_cte a join show_cte b
    on a.question_id = b.question_id
)
select question_id as survey_log
from answer_rate_cte
order by answer_rate desc, question_id
limit 1;