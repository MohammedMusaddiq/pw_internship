-- Write a query to list all details of all the managers


SELECT 
    emp_no, emp_name AS manager, salary, commission, hire_date
FROM
    employee
WHERE
    emp_no IN (SELECT DISTINCT
            manager_id
        FROM
            employee)
