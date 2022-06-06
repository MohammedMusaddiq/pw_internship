# 14. Write a Python program to check a dictionary is empty or not.

a = {}
b = {'a': 'hello', 'c': 'world', 'd': 'python', 'e': 'programming'}


def is_empty(dictionary):
    if len(dictionary) == 0:
        return print('The dictionary is empty')
    else:
        return print('The dictionary is Not empty')


is_empty(b)
