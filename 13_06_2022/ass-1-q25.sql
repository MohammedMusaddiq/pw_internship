--  Write a query in SQL to list the name of the managers who is having maximum number of employees working under him

SELECT a.emp_name,
       count(*)
FROM employee b,
     employee a
WHERE b.manager_id = a.emp_no
GROUP BY a.emp_name
HAVING count(*) =
  (SELECT MAX(mycount)
   FROM
     (SELECT COUNT(*) mycount
      FROM employee
      GROUP BY manager_id) a);

