# 12. Write a Python program to get the maximum and minimum value in a dictionary.

from random import randint

sample = {str(x): randint(10, 70) for x in range(1, 10)}
print('sample dict: ', sample)

dict_values = list(sample.values())

print("The max value in dict is: ", max(dict_values))
print("The min value in dict is: ", min(dict_values))
