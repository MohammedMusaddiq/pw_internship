<<<<<<< HEAD
-- 1. Fetch all the Customer Details along with the product names that the customer has ordered.

=======
>>>>>>> 2ac5bfc41b2009dbc0e5d4203e78aba39b57dae1
select c.customer_name, p.product_name, od.quantity
from customer c,
     product p,
     order_details od,
     `order` o
where c.customer_id = o.customer_id
  and p.product_id = od.product_id
  and o.order_id = od.order_id
order by c.customer_name;