# 1.Write a Python program to calculate the length of a string.

string = input("Enter a String: ")

#1st approach
print(len(string))

#2nd approach
length = 0
for i in string:
    length+=1
print(length)