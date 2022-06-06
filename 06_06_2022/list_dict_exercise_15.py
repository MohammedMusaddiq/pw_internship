# 15. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c': 300, }
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}
for k, v in d1.items():
    for k1, v1 in d2.items():
        if k == k1 and v == v1:
            d3[k1] = v + v1
        elif k != k1 and v != v1:
            d3[k] = v
            d3[k1] = v1

print('sample d1: ', d1)
print()
print('sample d2: ', d2)
print()
print('output: ', d3)
