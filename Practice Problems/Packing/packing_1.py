def max_tables(t: int, l: int) -> int:
    """
    Returns maximum number of square tables which can fit in a square loading area
    :param t: Table length
    :param l: Loading Area length
    """
    return (l // t) ** 2


assert max_tables(1, 1) == 1
assert max_tables(2, 4) == 4
assert max_tables(2, 5) == 4
assert max_tables(1, 4) == 16
assert max_tables(3, 16) == 25
assert max_tables(5, 18) == 9
assert max_tables(7, 77) == 121
assert max_tables(9, 8) == 0
assert max_tables(10, 499) == 2401
assert max_tables(17, 1819) == 11449
print("Passed")
