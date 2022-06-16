-- Write a query to display the details of employees who are senior to Martin



SELECT 
    emp_name, (YEAR(CURDATE()) - YEAR(hire_date)) AS experiance
FROM
    employee
WHERE
    (YEAR(CURDATE()) - YEAR(hire_date)) > (SELECT 
            (YEAR(CURDATE()) - YEAR(hire_date)) AS experiance
        FROM
            employee
        WHERE
            emp_name = 'Martin')