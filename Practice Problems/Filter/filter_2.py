from typing import List


def check_if_prime(num: int):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
    return True


def prime_sieve(nums: List[int]) -> List[int]:
    n = max(nums)
    toggles = [False, False] + ([True] * (n - 1))
    p = 2
    while p * p <= n:
        if not toggles[p]:
            p += 1
            continue
        for i in range(p * p, n + 1, p):
            toggles[i] = False
        p += 1
    return [n for n in nums if toggles[n]]


# Chooses between two approaches to minimise runtime.
def filter_primes(nums: List[int]) -> List[int]:
    size = len(nums)
    if size * size <= max(nums):  # sqrt(n) * O(sqrt(n))
        return [n for n in nums if check_if_prime(n)]
    else:
        return prime_sieve(nums)  # O(n log log n)


# Testing data below

test_a = [0, 3, 5, 8, 10, 11, 14, 19, 20]
test_b = [0, 0, 6, 7, 7, 9, 10, 13, 15, 19, 36]
test_c = [12, 19, 26, 30, 31, 32, 37, 45, 48, 77, 78, 81, 85, 95, 98]
test_d = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 24, 26, 27, 33, 35, 37, 39]
test_e = range(2, 1000)

assert filter_primes(test_a) == [3, 5, 11, 19]
assert filter_primes(test_b) == [7, 7, 13, 19]
assert filter_primes(test_c) == [19, 31, 37]
assert filter_primes(test_d) == [2, 3, 5, 7, 11, 13, 17, 19, 37]
assert filter_primes(test_e) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
print("Passed")
