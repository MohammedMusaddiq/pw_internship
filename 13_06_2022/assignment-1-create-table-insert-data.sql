CREATE TABLE depttable(deptno integer,dname text,loc text) 

INSERT INTO depttable (deptno,dname,loc)
VALUES(10 "Accounts" "Bangalore", 20 "IT " "Delhi", 30 "Production" "Chennai",40 "Sales" "Hyd",50 "Admn" "London");

CREATE TABLE EmpTable(
    EmpNo integer,
    Ename text,
    sal integer,
    Hire_Date date,
    Commission integer,
    DeptNo integer,
    Mgr integer
);

INSERT INTO emptable(empno, ename, sal, hire_date, commission, deptno, mgr)
VALUES (
    (1001, 'Sachin', '19000, '1-Jan-1980', 2100, 20, 1003),
    (1002, 'Kapil', 15000, '1-Jan-1970', 2300, 10, 1003),, 
    (1003, 'Stefen', 12000, '1-Jan-1990', 500, 20, 1007),,
    (1004, 'Williams', 9000, '1-Jan-2001', NULL, 30, 1007),
    (1005, 'John', 5000, '1-Jan-2005', NULL, 30, 1006),
    (1006, 'Dravid', 19000, '1-Jan-1985,' 2400, 10, 1007),
    (1007, 'Martin', 21000, '1-Jan-2000', 1040, NULL, NULL)

);