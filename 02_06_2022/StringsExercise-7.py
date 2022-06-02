# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

string = input("Enter a String: ")

find_not = string.find('not')
find_poor = string.find('poor')+4

if find_not < find_poor and find_not > 0 and find_poor > 0:
    string = string.replace(string[find_not:find_poor], 'good')

print(string)
