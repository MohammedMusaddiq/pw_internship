# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


empty_list_dict = [{}, {}, {}]
not_empty = [{}, {}, {'1': 2}]


def is_empty(x):
    r = all(len(i) == 0 for i in x)
    return print(r)


is_empty(not_empty)
