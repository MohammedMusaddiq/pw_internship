-- Fetch the customer details, who has placed multiple orders in the same year

SELECT 
    customer_id, YEAR(order_date), COUNT(*) as 'No of orders'
FROM
    `order`
GROUP BY customer_id , YEAR(order_date)
ORDER BY COUNT(*) DESC
LIMIT 1

-- approach 2

SELECT *
from (select *,
             case
                 when customer_id = lead(customer_id) over (
                     order by year(order_date)
                     )
                     and year(order_date) = lead(year(order_date)) over (
                         order by year(order_date)
                         ) then 'yes'
                 when customer_id = lag(customer_id) over (
                     order by year(order_date)
                     )
                     and year(order_date) = lag(year(order_date)) over (
                         order by year(order_date)
                         ) then 'yes'
                 else 'null'
                 end flag
      from `order`
      order by customer_id,
               year(order_date)) as x
where x.flag = 'yes'
