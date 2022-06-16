-- write a query to list the details and total experience of all the managers

SELECT 
    emp_name,
    hire_date,
    (YEAR(CURDATE()) - YEAR(hire_date)) AS experiance
FROM
    employee
WHERE
    emp_no IN (SELECT DISTINCT
            manager_id
        FROM
            employee)