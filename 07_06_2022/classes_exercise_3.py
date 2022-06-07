# # Write a Python class to get all possible unique subsets from a set of distinct integers
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]


class UniqueSubsets:
    def __init__(self, sample):
        self.sample = sample

    def get_subsets(self):
        subsets = [[]]
        for i in range(len(self.sample)):
            for j in range(len(subsets)):
                subsets.append(subsets[j] + [self.sample[i]])
        return subsets


us = UniqueSubsets([4, 5, 6])
print(us.get_subsets())
