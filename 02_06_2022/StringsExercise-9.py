# 9. Write a Python program to remove the nth index character from a nonempty string.

string = input("Enter the string: ")
index_value = int(input("Enter the index Position: "))

if len(string) != 0:
    try:
        string = string.replace(string[index_value], '')
        print(string)
    except IndexError:
        print("the given string length is less than index position")
