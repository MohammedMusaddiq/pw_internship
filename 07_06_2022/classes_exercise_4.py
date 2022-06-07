# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a
# specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4

numbers = [10, 20, 10, 40, 50, 60, 70]


class PairSum:

    def __init__(self, sample, target):
        self.target = target
        self.sample = sample
        self.output = ''

    def get_pair(self):
        for i in range(len(self.sample)):
            for j in range(i + 1, len(self.sample)):
                if self.sample[i] + self.sample[j] == self.target:
                    self.output = f'output: {i},{j}'
        print(self.output)


s = PairSum(numbers, 50)
s.get_pair()
