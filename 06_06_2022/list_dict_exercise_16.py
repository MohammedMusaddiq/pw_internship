# 16. Write a Python program to find the highest 3 values in a dictionary.

from random import randint

d = {x: randint(1, 500) for x in range(20)}
print()
print('the original dict: ', d)
d_values = list(d.values())
d_values.sort(reverse=True)
print()
print('top 3 values from dict: ', d_values[:3])
