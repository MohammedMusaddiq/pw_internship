-- Select Emp Details Whose experience is more than 2 years
SELECT * FROM `employee`
WHERE DATEDIFF(CURDATE(), `hire_date`) > 2