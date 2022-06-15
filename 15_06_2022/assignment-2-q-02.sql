-- 2. Fetch Order_Id, Ordered_Date, Total Price of the order (product price*qty).

select o.order_id, o.order_date, sum(p.product_price * od.quantity) as totla_price
from `order` o,
     order_details od,
     product p
where o.order_id = od.order_id
  and od.product_id = p.product_id
group by o.order_id, o.order_date

