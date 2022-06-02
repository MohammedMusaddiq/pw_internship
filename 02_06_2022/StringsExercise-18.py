# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

string = input("Enter a string: ")
new_string = ''
for i in string:
    if i == '.':
        i = ','
    elif i == ',':
        i = '.'
    new_string += i
print(new_string)
