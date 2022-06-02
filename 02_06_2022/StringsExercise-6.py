# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string = input("Enter a String: ")

end_char = string[-3:]

if len(string) >= 3:
    string = f'{string}ly' if end_char == 'ing' else f'{string}ing'
print(string)
