# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

string = input("Enter a string: ")

string_dict = {}
for i in string:
    if string.count(i) > 1:
        string_dict[i] = string.count(i)


output = sorted(string_dict.items(), key=lambda x: x[1], reverse=True)
for a, b in output:
    print(a, b)
