for i in range(5000):
    num = i + 1
    steps = 0

    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1

print("Finished")
