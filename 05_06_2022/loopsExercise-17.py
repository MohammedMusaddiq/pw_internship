# 17. Using range(1,101), make three list,
# one containing all even numbers
# one containing all odd numbers
# One containing only prime numbers

even_numbers = [i for i in range(1, 101) if i % 2 == 0]
odd_number = [i for i in range(1, 101) if i % 2 != 0]
prime_number = []
for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_number.append(i)


print("even numbers are")
print(even_numbers)
print()
print("odd numbers are")
print(odd_number)
print()
print("prime numbers are")
print(prime_number)
