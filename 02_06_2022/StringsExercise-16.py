# 16. Write a Python program to print the index of the character in a string.

string = input("Enter a string: ")

for i in string:
    print(i, string.find(i))
