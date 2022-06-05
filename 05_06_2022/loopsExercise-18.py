# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible
# by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

even_numbers = [i for i in range(1, 101) if i % 2 == 0]
odd_number = [i for i in range(1, 101) if i % 2 != 0]

new_list = even_numbers + odd_number

result = []
for i in new_list:
    conditions = [i % 4 == 0, i % 6 == 0, i % 8 == 0, i % 10 == 0, i % 3 == 0, i % 5 == 0, i % 7 == 0, i % 9 == 0]
    if any(conditions):
        result.append(i)
print(result)
