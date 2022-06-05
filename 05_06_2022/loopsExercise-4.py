#  4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
#  Note :
#  An equilateral triangle is a triangle in which all three sides are equal.
#  A scalene triangle is a triangle that has three unequal sides.
#  An isosceles triangle is a triangle with two equal sides.
#  Expected Output:
#  Input lengths of the triangle sides:
#  x: 6
#  y: 8
#  z: 12
#  Scalene triangle

x, y, z = input("Enter value for x, y, z: ").split()

if x == y == z == x:
    print("equilateral triangle")
elif x == y or y == z or z == x:
    print("isosceles triangle")
else:
    print("scalene triangle")
