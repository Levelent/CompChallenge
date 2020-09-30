max_strength = 0
max_strength_start = 0

for i in range(5000):
    num = i + 1
    start_num = num
    strength = 0

    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        strength += 1

    if strength > max_strength:
        max_strength = strength
        max_strength_start = start_num

print(f"Maximum Strength: {max_strength} | Number: {max_strength_start}")
