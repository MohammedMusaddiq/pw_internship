# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

num_list = []
for _ in range(10):
    integers = int(input("Enter the Numbers: "))
    num_list.append(integers)
avg = (sum(num_list) / len(num_list))
print(round(avg, 2))
