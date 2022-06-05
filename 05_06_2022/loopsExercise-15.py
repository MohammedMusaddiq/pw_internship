# 15. Take integer inputs from user until he/she presses q
# ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

exit_word = ''

product = 1
count = 0
while True:
    numbers = input("Enter any number|press 'q' to quit: ")
    if numbers == 'q':
        break
    product *= int(numbers)
    count += 1

print(f"The average of given numbers is {product / count}")
print(f"The product of given numbers is {product}")
