-- 5. Fetch the Customer name along with the total Purchase Amount

SELECT c.customer_name, SUM(ord.Quantity * p.product_price) as Total_Amount
from Customer c
         inner join `order` o
         inner join product p
         inner join order_details ord
                    on c.customer_id = o.customer_id
                        and o.order_id = ord.order_id
                        and ord.product_id = p.product_id
Group By c.customer_id