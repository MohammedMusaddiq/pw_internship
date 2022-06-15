-- Fetch the customer details , who has placed more number of orders

select c.customer_id, c.customer_name, count(*) as order_count
from customer c,
     `order` o
where c.customer_id = o.customer_id
group by c.customer_id
order by order_count desc
limit 1;




