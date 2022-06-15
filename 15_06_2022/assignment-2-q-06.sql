-- Fetch the Customer details, who has placed the first and last order


-- Fetch the Customer details, who has placed the first and last order

select customer_id, min(order_date),max(order_date)
from `order`
group by customer_id
order by min(order_date)
limit 1








