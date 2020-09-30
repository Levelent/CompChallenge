encountered_above_limit = set()

for i in range(5000):
    num = i + 1
    steps = 0

    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        if num > 5000:
            encountered_above_limit.add(num)

num_above = len(encountered_above_limit)
unique_nums = num_above + 5000
print(f"Above Limit: {num_above/unique_nums * 100:.2f}% | Highest Num: {max(encountered_above_limit)}")
