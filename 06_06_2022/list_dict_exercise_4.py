# 4. Write a Python script to check if a given key already exists in a dictionary.

sample_dict = {'apple': 1, 'mango': 2, 'grapes': 3, 'kivi': 4, 'orange': 5}
qry = input("Enter the key to find in dictionary: ")
if sample_dict.get(qry) is not None:
    print("The given key exists in dictionary: ", {qry: sample_dict.get(qry)})
else:
    print("The key does not exists in dictionary")
