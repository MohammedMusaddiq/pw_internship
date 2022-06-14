-- Fetch Dept Name , Total Salry of the Dept

SELECT department.department_name, salary.total_amt
FROM department,
( SELECT employee.department_no, SUM(employee.salary) AS total_amt
FROM employee  
GROUP BY department_no) AS salary
WHERE salary.department_no = department.department_no;