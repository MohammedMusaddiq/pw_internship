# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and
# the perimeter of a circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        return round(3.14 * self.radius ** 2, 2)

    def perimeter_of_circle(self):
        return round(2 * 3.14 * self.radius, 2)


circle = Circle(5)
print(circle.area_of_circle())
print(circle.perimeter_of_circle())
