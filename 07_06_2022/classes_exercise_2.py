# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and
# "{{{" are invalid.


class MatchParentheses:
    def __init__(self, string):
        self.string = string
        self.parentheses = {'(': ')', '[': ']', '{': '}'}
        self.container = []

    def is_valid(self):
        for char in self.string:
            if char in self.parentheses:
                self.container.append(char)
            elif char in self.parentheses.values():
                if len(self.container) == 0:
                    return False
                if self.parentheses[self.container.pop()] != char:
                    return False
        return len(self.container) == 0


mp = MatchParentheses('(]')
print(mp.is_valid())
