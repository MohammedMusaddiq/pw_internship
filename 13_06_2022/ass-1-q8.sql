-- Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.

SELECT e.* , d.department_name,d.location 
FROM 
employee AS e,
department AS d
WHERE e.department_no=d.department_no