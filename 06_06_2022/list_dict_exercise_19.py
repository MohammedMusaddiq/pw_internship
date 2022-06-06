# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print('original list: ', l1)
print()
print('after removing duplicates: ', l2)
