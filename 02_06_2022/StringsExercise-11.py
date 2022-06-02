# 11. Write a Python function to reverses a string if it's length is a multiple of 4

string = input("Enter a String: ")

len_of_string = len(string)

if len_of_string % 4 == 0:
    string = string[::-1]

print(string)
