from typing import List
from itertools import combinations


def filter_sums(nums: List[int]) -> List[int]:
    idx_combs = combinations(range(len(nums)), 2)

    sum_data = []
    for tup in idx_combs:
        this_sum = nums[tup[0]] + nums[tup[1]]
        sum_data.append([this_sum, tup[0], tup[1]])

    filtered = []
    for i in range(len(nums)):
        for s in sum_data:
            if s[0] == nums[i] and s[1] != i != s[2]:
                break
        else:
            filtered.append(nums[i])

    return filtered


# Testing data below
test_a = [0, 3, 5, 8, 10, 11, 14, 19, 20]
test_b = [0, 0, 6, 7, 7, 9, 10, 13, 15, 19, 36]
test_c = [0, 0, 0, 12, 19, 26, 30, 31, 32, 37, 45, 48, 77, 78, 81, 85, 95, 98]

assert filter_sums(test_a) == [0, 3, 5, 10, 20]
assert filter_sums(test_b) == [0, 0, 6, 9, 10, 36]
assert filter_sums(test_c) == [12, 19, 26, 30, 32, 37, 48, 81, 95, 98]
print("Passed")
