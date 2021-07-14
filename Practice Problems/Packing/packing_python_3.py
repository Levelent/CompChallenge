from typing import List, Tuple


def area_remaining(small_w: int, small_h: int, large_w: int, large_h: int) -> int:
    """
    Given that packages can only be rotated at 90 degree angles
    Determines whether a smaller, rectangular box can fit in a larger, rectangular box (environmentally friendly)
    :param small_w:
    :param small_h:
    :param large_w:
    :param large_h:
    :returns int: The area remaining after the first package is fitted inside the second. -1 if no fit.
    """
    m = min(small_w, small_h)
    n = max(small_w, small_h)
    x = min(large_w, large_h)
    y = max(large_w, large_h)

    if n > y and m < x:
        print(f"m = {m}, n = {n}, x = {x}, y = {y}")
        term_1 = ((y + x) / (n + m))
        term_2 = ((y - x) / (n - m))
        ans = term_1 * term_1 + term_2 * term_2
        print(ans)
        if ans >= 2:
            return (x * y) - (n * m)
        else:
            return -1

    if m <= x and n <= y:
        return (x * y) - (n * m)
    return -1


def efficient_packing(packages: List[Tuple[int, int]], containers: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Determines which 2D packages should be fit inside which 2D containers to ensure that of the containers used, the least area is wasted.
    Packages and containers can be freely rotated.
    :param packages:
    :param containers:
    """
    values = []
    for pack in packages:
        all_cont_for_pack = []
        for cont in containers:
            all_cont_for_pack.append(area_remaining(pack[0], pack[1], cont[0], cont[1]))
        values.append(all_cont_for_pack)

    print(values)

    # Unfinished, appears to need something along the lines of the hungarian algorithm.

    return 0, 0


print(efficient_packing([(1, 2), (1, 2), (9, 8), (3, 4), (5, 2), (2, 5)], [(3, 3), (3, 4), (6, 9), (4, 6), (19, 36), (2, 2)]))

# Diagonal Plates Examples
# assert max_plates(1, 3, 2, 2) == 0
# assert max_plates(1, 7, 5, 6) == 0
# assert max_plates(1, 6, 5, 5) == 1
#
# assert max_plates(1, 7, 6, 6) == 1
# assert max_plates(2, 47, 40, 40) == 4
