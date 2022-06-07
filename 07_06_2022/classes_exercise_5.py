# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


sample_list = [-25, -10, -7, -3, 2, 4, 8, 10]


class SumOfThree:

    def __init__(self, sample):
        self.result = []
        self.sample = sample
        self.length = len(sample)

    def find_three_elements(self):
        for i in range(self.length):
            for j in range(i + 1, self.length):
                for k in range(j + 1, self.length):
                    if self.sample[i] + self.sample[j] + self.sample[k] == 0:
                        self.result.append([self.sample[i], self.sample[j], self.sample[k]])
        print(self.result)


s = SumOfThree(sample_list)
s.find_three_elements()
