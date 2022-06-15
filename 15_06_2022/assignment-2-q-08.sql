-- Fetch the customer details, who has placed multiple orders in the same year

select customer_id, year(order_date), count(*)
from `order`
group by customer_id,year(order_date)
order by count(*) desc
limit 1


