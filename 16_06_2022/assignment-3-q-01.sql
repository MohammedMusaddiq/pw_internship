-- 1. Write a query to display the employee details, department details and the manager details of the employee who has second highest salary

with salary_cte as (
    select
        e.emp_no,
        e.emp_name,
        e.salary,
        d.department_name,
        dense_rank() over(
            order by
                salary desc
        ) as sal_ord
    from
        employee e
        left join employee m on e.manager_id = m.emp_no
        left join department d on e.department_no = d.department_no
)
select
    *
from
    salary_cte
where
    sal_ord = 2

