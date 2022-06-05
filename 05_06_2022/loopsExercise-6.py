#  6. Write a Python program to construct the following pattern, using a nested loop number.
#  1
#  22
#  333
#  4444
#  55555
#  666666
#  7777777
#  88888888
#  999999999

# 1st approach
for i in range(1, 10):
    print(str(i)*i)

# 2st approach
for i in range(1, 10):
    for _ in range(i):
        print(i, end="")
    print()
