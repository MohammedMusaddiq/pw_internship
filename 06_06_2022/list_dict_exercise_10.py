# 10. Write a Python program to remove a key from a dictionary.

sample = {'val1': 100, 'val2': 200, 'val3': 300, 'val4': 400, 'val5': 500}
qry = input('Enter key value: ')
print()
print('initial dict: ', sample)
print()
sample.pop(qry)
print('dict after removing key: ', sample)
