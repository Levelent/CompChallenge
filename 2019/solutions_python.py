from typing import List


# Challenge A

def quad(a: int, b: int, c: int) -> str:
    """
    Returns the string representation of a quadratic equation, given the co-efficients of each term
    """

    quad_str = ""

    # a is never 0, so will always be added
    if abs(a) != 1:  # Coefficient isn't 1 or -1
        quad_str += str(a)
    elif a == -1:
        quad_str += "-"
    quad_str += "x^2"

    if b != 0:
        if b > 0:
            quad_str += "+"  # Positive, non-starting term
        if abs(b) != 1:
            quad_str += str(b)
        elif a == -1:
            quad_str += "-"
        quad_str += "x"

    if c != 0:
        if c > 0:
            quad_str += "+"
        # Constant terms will always have coeffs
        quad_str += str(c)

    quad_str += "=0"
    return quad_str


print("Challenge A | Quad")
# Note that "x^2 + 2x + 3 = 0" and "x^2+2x+3=0" are both equally valid
assert quad(1, 2, 3) == "x^2+2x+3=0"
assert quad(-3, 4, -10) == "-3x^2+4x-10=0"
assert quad(-1, 0, 1) == "-x^2+1=0"


# Challenge B

def quad_root(alpha: int, beta: int) -> str:
    """
    Returns the string representation of a quadratic, given the roots of the equation
    """

    # (x - alpha)(x - beta) = 0 can be expanded out to obtain
    # x^2 - (alpha + beta) x + (alpha * beta) = 0
    return quad(1, -(alpha+beta), alpha*beta)


print("Challenge B | QuadRoot")
assert quad_root(6, 9) == "x^2-15x+54=0"
assert quad_root(-80, 0) == "x^2+80x=0"
assert quad_root(7, -7) == "x^2-49=0"


# Challenge C

def poly(coeffs: List[int]) -> str:
    """
    Returns the string representation of a polynomial, given the co-efficients of each term
    """
    poly_str = ""
    for pos, coeff in enumerate(coeffs):

        if pos != 0 and coeff > 0:  # positive, non-leading term
            poly_str += "+ "

        if coeff < 0:
            poly_str += "- "

        if coeff != 0:
            # Either number isn’t -1, 0, 1, or it’s the last term
            if abs(coeff) > 1 or pos == len(coeffs) - 1:
                poly_str += str(abs(coeff))  # abs() to avoid repeated minus sign

            poly_str += f"x^{len(coeffs) - 1 - pos} "

    poly_str = poly_str.replace("x^0", "")  # Anything to the power of 0 is 1
    poly_str = poly_str.replace("x^1 ", "x ")  # The space prevents "x^11" being turned into "x1"
    return poly_str + "= 0"


print("Challenge C | Poly")
assert poly([-3, 4]) == "- 3x + 4 = 0"
assert poly([8, -6, -1, 1, -5, 2]) == "8x^5 - 6x^4 - x^3 + x^2 - 5x + 2 = 0"
assert poly([1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 8, 3]) == "x^11 - x^7 + 8x + 3 = 0"


# Challenge D


def poly_root(root_list):
    coefficients = [1]  # The first coefficient will always be 1
    multi = -1
    for i in range(len(root_list)):
        coeff = multi * combinations(root_list, i + 1)
        coefficients.append(coeff)

        multi *= -1  # Mimics the alternating + - behaviour of the coefficients.

    return poly(coefficients)  # We already have a way to format our answer


# A recursive approach to the problem
def combinations(comb_list, depth):
    total = 0
    if depth == 1:
        # We’ve reached the bottom, so should add all remaining values
        for combination in comb_list:
            total += combination
        return total

    for i in range(len(comb_list) - depth + 1):
        # All items in the list after position i
        remaining = comb_list[(i + 1):]

        # Find the combinations of the remaining list, and multiply
        other_combs = combinations(remaining, depth - 1)
        total += comb_list[i] * other_combs

    return total


print("Challenge D | PolyRoot")
assert poly_root([-3]) == "x + 3 = 0"
assert poly_root([8, -6, -1, 1, -5, 2]) == "x^6 + x^5 - 65x^4 - 125x^3 + 544x^2 + 124x - 480 = 0"
assert poly_root([1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 8, 3]) == "x^12 - 11x^11 + 23x^10 + 11x^9 - 24x^8 = 0"
