--Write a query to fetch number of employees in each location


SELECT COUNT(*) AS no_of_employees, depttable.loc
FROM depttable
INNER JOIN emptable ON depttable.deptno = emptable.deptno
GROUP BY depttable.loc