import timeit


def digit_sum(n: int):
    return sum([int(c) for c in str(n)])


# Building on part 1
def digital_root_a(n: int):
    while n > 9:
        n = digit_sum(n)
    return n


# More efficient solution
def digital_root_b(n: int):
    a = n % 9
    if a == 0 and n != 0:
        return 9
    return a


max_n = 10000000

start_time = timeit.default_timer()
for i in range(max_n):
    assert digital_root_a(i) == digital_root_b(i)
print(f"Execution Time: {timeit.default_timer() - start_time}")

start_time = timeit.default_timer()
for i in range(max_n):
    digital_root_b(i)
print(f"Execution Time: {timeit.default_timer() - start_time}")

