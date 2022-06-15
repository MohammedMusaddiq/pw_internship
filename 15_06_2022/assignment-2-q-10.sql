-- 10. Fetch the maximum priced Ordered Product

select p.product_name, p.product_price
from product p
         join order_details od on od.product_id = p.product_id
order by p.product_price desc
limit 1;



