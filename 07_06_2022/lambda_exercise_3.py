# 3) Write a Python program to sort a list of dictionaries using Lambda.

# Original list of dictionaries : [{'make':'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
#                                   'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
#                                       'color': 'Blue'}, {'make': 'Mi Max', 'model': '2','color': 'Gold'}]


sample = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_sample = sorted(sample, key=lambda x: int(x['model']), reverse=True)
print(sorted_sample)
