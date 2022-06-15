-- 9. Fetch the name of the month, in which more number of orders has been placed

select month(order_date) as month, count(*) as count
from `order`
group by month
order by count desc
limit 1;





