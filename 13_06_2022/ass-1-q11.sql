-- Get Employee Name and gross salary (sal + comission) 

SELECT employee.emp_name, employee.salary+employee.commission AS 'gross salary' FROM employee