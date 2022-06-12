# Write your MySQL query statement below

Select id,
ifnull(case when id % 2 != 0
        then lead(student) over()
        else lag(student) over()
        end, student) as student
from seat