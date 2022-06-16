-- Fetch the Customer details, who has placed the first and last order

SELECT 
    customer_id, MIN(order_date), MAX(order_date)
FROM
    `order`
GROUP BY customer_id
ORDER BY MIN(order_date)
LIMIT 1








