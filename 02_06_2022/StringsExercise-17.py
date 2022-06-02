# 17. Write a Python program to convert a string in a list.

string = input("Enter a string: ").replace(" ", "")
string_to_list = []
for i in string:
    string_to_list.append(i)
print(string_to_list)
