# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

x = {'name': 'musaddiq', 'age': 24, 'place': 'India'}
y = {'name': 'umar ', 'age': 24}

for k, v in x.items():
    for k1, v1 in y.items():
        if k == k1 and v == v1:
            print(f"{k}: {v} present in both x and y")
        else:
            pass
