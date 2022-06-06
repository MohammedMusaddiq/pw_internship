# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

old_dict = {0: 10, 1: 20}
print('old dictionary', old_dict)
old_dict.update({2: 30})
print()
print('dictionary with updated key, value', old_dict)
