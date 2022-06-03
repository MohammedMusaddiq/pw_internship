# 20. Write a Python program to remove all consecutive duplicates of a given string.

string = input("Enter a string: ")


output = string[0]
count = 1

for x in string:
    if x != output[count-1]:
        output += x
        count += 1

print(output)
