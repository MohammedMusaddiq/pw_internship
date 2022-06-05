# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

inputs = input("Enters Numbers to create a list(space separated): ").split()
inp_list = [int(i) for i in inputs]


# 1st approach
count = 0
for i in inp_list:
    if i > 30:
        count += 1
print(f"number of elements greater than 30 in the list = {count}")

# 2nd approach
count = sum(i > 30 for i in inp_list)
print(f"number of elements greater than 30 in the list = {count}")

