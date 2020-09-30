import timeit


def collatz(limit: int):
    print(f"Limit: {limit}")
    max_strength = 0
    max_strength_start = 0
    above_limit = set()

    for i in range(limit):
        num = i + 1
        start_num = num
        strength = 0

        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num * 3) + 1
            if num > limit:
                above_limit.add(num)
            strength += 1

        if strength > max_strength:
            max_strength = strength
            max_strength_start = start_num

    print(f"Maximum Strength: {max_strength} | Number: {max_strength_start}")
    num_above = len(above_limit)
    unique_nums = num_above + limit
    print(f"Above Limit: {num_above/unique_nums * 100:.2f}% | Highest Num: {max(above_limit, default=limit)}")


start_time = timeit.default_timer()
collatz(1000000)
print(f"Execution Time: {timeit.default_timer() - start_time}")
