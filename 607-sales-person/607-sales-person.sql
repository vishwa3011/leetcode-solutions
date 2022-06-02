# Write your MySQL query statement below


select name from SalesPerson
where name not in (
    Select sp.name 
    from SalesPerson sp inner join orders o
    on sp.sales_id = o.sales_id inner join company c
    on o.com_id = c.com_id
    where c.name = 'RED'
)

