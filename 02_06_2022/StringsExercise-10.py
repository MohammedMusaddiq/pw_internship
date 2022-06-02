# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

string = input("Enter Coma Separated Words: ")
string = string.replace(" ", "")
list_string = string.split(',')
list_string = sorted(set(list_string))
output = ", ".join(list_string)

print(output)
