-- Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)
SELECT REPLACE(`emp_name`, 'a', '#') FROM `employee`