from typing import List


def filter_multiples(numbers: List[int]) -> List[int]:
    new_numbers = []
    for num in numbers:
        if num % 5 != 0:
            new_numbers.append(num)
    return new_numbers


# Testing data below

test_a = [0, 3, 5, 8, 10, 11, 14, 19, 20]
test_b = [0, 0, 6, 7, 7, 9, 10, 13, 15, 19, 36]
test_c = [12, 19, 26, 30, 31, 32, 37, 45, 48, 77, 78, 81, 85, 95, 98]

assert filter_multiples(test_a) == [3, 8, 11, 14, 19]
assert filter_multiples(test_b) == [6, 7, 7, 9, 13, 19, 36]
assert filter_multiples(test_c) == [12, 19, 26, 31, 32, 37, 48, 77, 78, 81, 98]
print("Passed")
