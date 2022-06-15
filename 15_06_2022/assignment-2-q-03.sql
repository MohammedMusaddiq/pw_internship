-- 3. Fetch the Customer Name, who has not placed any order

select customer_name
from customer
     where customer_id not in (select customer_id
                                from `order`)

