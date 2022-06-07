# Write your MySQL query statement below

with approved
as
(
Select id, country, state, amount, date_format(trans_date,'%Y-%m') as month
    from transactions
    where state = 'approved'
),

chargebacks
as
(
select trans_id, t.country, "chargeback" as state, t.amount, date_format(c.trans_date,'%Y-%m') as month
    from Chargebacks c left join Transactions t
    on c.trans_id = t.id
),

combined
as
(
select * from approved
UNION ALL
select * from chargebacks
)

Select month, country,
sum(case when state = "approved" then 1 else 0 end) as approved_count,
sum(case when state = "approved" then amount else 0 end) as approved_amount,
sum(case when state = "chargeback" then 1 else 0 end) as chargeback_count,
sum(case when state = "chargeback" then amount else 0 end) as chargeback_amount
from combined
group by country, month

# Select c.month, c.country, coalesce(a.approved_count,0) as approved_count, coalesce(a.approved_amount,0) as approved_amount, coalesce(c.chargeback_count,0) as chargeback_count, coalesce(c.chargeback_amount,0) as chargeback_amount
# from approved a left join chargebacks c
# on a.month = c.month
# UNION ALL
# Select c.month, c.country, coalesce(a.approved_count,0) as approved_count, coalesce(a.approved_amount,0) as approved_amount, coalesce(c.chargeback_count,0) as chargeback_count, coalesce(c.chargeback_amount,0) as chargeback_amount
# from approved a right join chargebacks c
# on a.month = c.month
