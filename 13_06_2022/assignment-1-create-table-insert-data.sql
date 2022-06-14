CREATE TABLE `department` (
    `department_no` INT,
    `department_name` VARCHAR(45),
    `location` VARCHAR(45),
    PRIMARY KEY (`department_no`)
);

INSERT INTO `department` VALUES (10,'Accounts','Bangalore');
INSERT INTO `department` VALUES (20,'IT','Delhi');
INSERT INTO `department` VALUES (30,'Production','Chennai');
INSERT INTO `department` VALUES (40,'Sales','Hyd');
INSERT INTO `department` VALUES (50,'Admin','London');


CREATE TABLE `employee` (
    `emp_no` INT,
    `emp_name` VARCHAR(45),
    `salary` INT,
    `hire_date` DATE,
    `commission` INT,
    `department_no` INT,
    `manager_id` INT,
    PRIMARY KEY (`emp_no`),
    FOREIGN KEY (`department_no`) REFERENCES `department`(`department_no`),
    FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_no`)
);
INSERT INTO `employee` VALUES (1001,'Sachin',19000,'1990-01-01',2100,20,1003);
INSERT INTO `employee` VALUES (1002,'Kapil',15000,'1970-01-01',2300,10,1003);
INSERT INTO `employee` VALUES (1003,'Stefen',12000,'1990-01-01',500,20,1007);
INSERT INTO `employee` VALUES (1004,'Williams',9000,'2001-01-01',NULL,30,1007);
INSERT INTO `employee` VALUES (1005,'John',5000, '2005-01-01',NULL,30,1006);
INSERT INTO `employee` VALUES (1006,'Dravid',19000,'1985-01-01',2400,10,1007);
INSERT INTO `employee` VALUES (1007,'Martin',21000,'2000-01-01',1040,NULL,NULL);

    
