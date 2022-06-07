# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.
# Sample Output:
# 25
# 48

add_15 = lambda x: x + 15
print(add_15(10))

multiply_x_y = lambda x, y: x * y
print(multiply_x_y(6, 8))
