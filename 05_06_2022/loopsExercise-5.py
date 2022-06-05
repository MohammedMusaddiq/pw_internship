# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user).
# Input 0 to finish

while True:
    integers = input(
    "Enter some integers to calculate sum and their average(space separated): ").split()
    integers_list = [int(i) for i in integers]
    if len(integers_list)<2 and integers_list[0] == 0:
        break
    sum_of_int = sum(integers_list)
    avg_of_int = sum_of_int / len(integers_list)
    print(f"sum of given integers is '{sum_of_int}'")
    print(f"average of given integers is '{avg_of_int}'")
