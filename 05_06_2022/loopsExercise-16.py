# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete
# that element, if found. Iterate over list using for loop.

user_list = input("Enter values to create a list(separated by space): ").split()
query = input("Enter the value to find and delete from list:  ")
print()
print("The initial list:")
print(user_list)
print()
if query in user_list:
    user_list.remove(query)
    print(f"The list after removing '{query}':")
    print(user_list)
