# 11. Write a Python program to sort a dictionary by key.

sample = {'c': 10, 'b': 20, 'a': 30,}

print('sample dict with out sorting: ', sample, end='\n')
sort = dict(sorted(sample.items(), key=lambda x: x[0]))
print('sample dict after sorting: ', sort)
