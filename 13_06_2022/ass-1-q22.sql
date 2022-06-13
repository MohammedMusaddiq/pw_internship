-- Get the details of the employees who works in Bangalore location

SELECT * FROM emptable
INNER JOIN depttable
ON emptable.deptno=depttable.deptno
WHERE depttable.loc='Bangalore'
