# 7) Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'


class ReverseString:
    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        return ' '.join(self.string.split()[::-1])


reverse_string = ReverseString('hello .py')
print(reverse_string.reverse_string())


