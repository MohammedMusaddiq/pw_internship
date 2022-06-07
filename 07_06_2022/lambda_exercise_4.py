# 4) Write a Python program to find if a given string starts with a given character using Lambda.

string = 'hello world'
qry = input("Enter the character: ")

check = lambda x, y: bool(x.startswith(y))
print(check(string, qry))
