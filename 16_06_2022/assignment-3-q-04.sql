-- Write a query to list the employees who is manager and  takes commission less than 1000 and works in Delhi

SELECT 
    e.emp_name, d.department_name
FROM
    employee e
        LEFT JOIN
    department d ON e.department_no = d.department_no
WHERE
    e.emp_no IN (SELECT DISTINCT
            manager_id
        FROM
            employee)
        AND e.commission < 1000
        AND d.location = 'Delhi'