# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

string1 = input("Enter string one: ")
string2 = input("Enter string two: ")

string1_char = string1[:2]
string2_char = string2[:2]

string1 = string1.replace(string1_char, string2_char)
string2 = string2.replace(string2_char, string1_char)

output = f"{string1} {string2}"
print(output)
