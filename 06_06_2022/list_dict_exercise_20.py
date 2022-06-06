# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

l1 = [10, 20, 30]
l2 = [40, 50, 60]

l1 = l2 + l1

print(l1)
