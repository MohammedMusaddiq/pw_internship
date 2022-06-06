# 3. Write a Python program to remove duplicates from Dictionary.

sample = {'a': 'hello', 'b': 'hello', 'c': 'world', 'd': 'python', 'e': 'programming', 'f': 'python', }
print('sample dict:', sample, end='\n')
result = {}

for k, v in sample.items():
    if v not in result.values():
        result[k] = v
print('unique dict: ', result)
