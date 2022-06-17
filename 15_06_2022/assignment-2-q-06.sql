-- Fetch the Customer details, who has placed the first and last order



with date_cte as (
    select
        customer_id,
        order_date,
        dense_rank() over(
            order by
                order_date desc
        ) as date_ord
    from
        `order`
)
select
    customer_id,
    order_date as 'order dates'
from
    date_cte
where
    date_ord = 1
    or date_ord = 10;






