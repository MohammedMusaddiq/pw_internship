-- Write a statement to delete employees belong to Chennai location.

DELETE a 
FROM employee as a
JOIN department as b 
ON a.department_no = b.department_no
AND b.location = 'Chennai'
