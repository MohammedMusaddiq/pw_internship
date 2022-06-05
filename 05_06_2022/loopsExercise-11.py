# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

m = int(input("Enter your marks: "))

if m < 25:
    print("your grade is 'F'")
elif 25 <= m <= 45:
    print("your grade is 'E'")
elif 45 < m <= 50:
    print("your grade is 'D'")
elif 50 < m <= 60:
    print("your grade is 'C'")
elif 60 < m <= 80:
    print("your grade is 'B'")
else:
    print("your grade is 'A'")
