# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter,
# a number and a minimum length using lambda.
# Minimum length : 10
# input string: PaceWisd0m
# o/p: valid string

string = 'PaceWisd0m'
condition = [any(i.isupper() for i in string), any(i.islower for i in string), any(i.isnumeric() for i in string)]
var = lambda x: print('valid string') if all(condition) else print('not a valid string')

var(string)
