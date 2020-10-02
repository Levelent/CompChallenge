def max_plates(box_x: int, box_y: int, load_x: int, load_y: int) -> int:
    """
    Returns maximum number of plate sets that can fit inside a rectangular loading area
    :param box_x:
    :param box_y:
    :param load_x:
    :param load_y:
    """

    options = []
    for orient_a, orient_b in [(load_x, load_y), (load_y, load_x)]:
        quot_w, rem_w = divmod(orient_a, box_x)
        quot_h, rem_h = divmod(orient_b, box_y)

        base = quot_h * quot_w
        print(f"Initial Box: {base}")

        if rem_w == rem_h == 0:
            return quot_h * quot_w
        elif rem_w // box_y != 0:
            extra = rem_w // box_y * orient_b // box_x
            print(f"Extra from width: {extra}")
        else:
            extra = rem_h // box_x * orient_a // box_y
            print(f"Extra from height: {extra}")

        options.append(base + extra)

    return max(options)


assert max_plates(1, 2, 2, 1) == 1
assert max_plates(1, 2, 3, 3) == 4
assert max_plates(1, 2, 3, 4) == 6
assert max_plates(9, 8, 6, 9) == 0
assert max_plates(3, 4, 4, 6) == 2
assert max_plates(5, 2, 19, 36) == 68
assert max_plates(2, 5, 19, 36) == 68

# Partial Solution, does not pass the below tests

# Diagonal Plates Examples
assert max_plates(1, 6, 5, 5) == 1
assert max_plates(2, 47, 40, 40) == 4
# 3rd multiple diagonal

print("Passed")
