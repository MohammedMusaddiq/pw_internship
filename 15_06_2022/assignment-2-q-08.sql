-- Fetch the customer details, who has placed multiple orders in the same year

SELECT 
    customer_id, YEAR(order_date), COUNT(*) as 'No of orders'
FROM
    `order`
GROUP BY customer_id , YEAR(order_date)
ORDER BY COUNT(*) DESC
LIMIT 1
