-- 4. Fetch the Product Details without any order(purchase)

select product_name
from product
where product_id not in (select product_id from order_details)
