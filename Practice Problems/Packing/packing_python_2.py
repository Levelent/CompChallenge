
def max_plates(small_w: int, small_h: int, large_w: int, large_h: int) -> int:
    """
    Given that the items can only be rotated at 90 degree angles, and can't overlap,
    determines how many smaller items can fit inside a larger one.
    :param small_w:
    :param small_h:
    :param large_w:
    :param large_h:
    """
    m = min(small_w, small_h)
    n = max(small_w, small_h)
    x = min(large_w, large_h)
    y = max(large_w, large_h)

    if m > x or n > y:
        return 0

    options = []
    for orient_a, orient_b in [(large_w, large_h), (large_h, large_w)]:
        quot_w, rem_w = divmod(orient_a, small_w)
        quot_h, rem_h = divmod(orient_b, small_h)

        base = quot_h * quot_w
        print(f"Initial Box: {base}")

        if rem_w == rem_h == 0:
            return quot_h * quot_w
        elif rem_w // small_h != 0:
            extra = rem_w // small_h * orient_b // small_w
            print(f"Extra from width: {extra}")
        else:
            extra = rem_h // small_w * orient_a // small_h
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

print("Passed")
