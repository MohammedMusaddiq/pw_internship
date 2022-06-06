# 9. Write a Python program to multiply all the items in a dictionary.

sample = {'val1': 100, 'val2': 200, 'val3': 300, 'val4': 400, 'val5': 500}

result = 1

for x in sample.values():
    result *= x

print("Result by multiplying dict values: ", result)
