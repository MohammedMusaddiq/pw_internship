# 6) Write a Python class to implement pow(x, n)

class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def get(self):
        return self.x ** self.n


p = Pow(2, 3)
print(p.get())