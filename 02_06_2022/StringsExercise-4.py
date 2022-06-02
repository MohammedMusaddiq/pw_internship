# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = input("Enter a String: ")
first_char = string[0]
remaining_char = string[1:]
remaining_char = remaining_char.replace(first_char, '$')
string = first_char + remaining_char
print(string)
