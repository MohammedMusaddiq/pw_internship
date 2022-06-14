-- Write a query to fetch all the dept details with more than 1 Employee.

SELECT department.department_name, COUNT(*) AS `number of employees`
  FROM department 
     INNER JOIN employee
       ON department.department_no = employee.department_no
        GROUP BY department.department_name
          HAVING COUNT(*) > 1;