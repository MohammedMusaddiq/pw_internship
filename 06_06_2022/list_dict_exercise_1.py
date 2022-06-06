# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

dictionary = {
    'a': 7,
    'b': 12,
    'c': 8,
    'd': 10,
    'e': 16,
    'f': 15,
}

sorted_ascending = sorted(dictionary.items(), key=lambda x: x[1])
sorted_descending = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

sorted_dict_a = dict(sorted_ascending)
sorted_dict_d = dict(sorted_descending)

print('original dictionary', dictionary)
print()
print('sorted dictionary ascending', sorted_dict_a)
print()
print('sorted dictionary descending', sorted_dict_d)
