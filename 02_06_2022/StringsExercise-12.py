# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

string = input("Enter a String: ")
char = string[:4]
count = 0
for x in char:
    if x.isupper():
        count += 1
if count >= 2:
    string = string.upper()

print(string)
