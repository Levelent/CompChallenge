from typing import List


# Section A (35 Points)


def chain(grid: List[List[str]]) -> bool:

    return True


def tic_tac_toe(grid: List[List[str]]) -> bool:

    return True


# Section B (65 Points)


def max_chain(grid: List[List[str]]) -> int:

    return 0


def tic_tac_no(n: int) -> int:

    return 0


def chain_blocker(n: int, k: int) -> List[List[str]]:

    return [["B", "U"], ["B", "U"]]


# --------------------------------------------------
# You don't need to modify anything below this line
# --------------------------------------------------


def grid_input(letter, func):
    with open(f"inputs/input_{letter}.txt") as file:
        gs = file.read().split("\n\n")
    outputs = []
    print(f"------ Challenge {letter.upper()} ------")
    for g in gs:
        grid = [list(row) for row in g.split("\n")]
        outputs.append(func(grid))
    return outputs


def integer_input(letter, func):
    with open(f"inputs/input_{letter}.txt") as file:
        nums = [int(n) for n in file.read().split("\n")]
    outputs = []
    print(f"------ Challenge {letter.upper()} ------")
    for num in nums:
        outputs.append(func(num))
    return outputs


def two_integer_input(letter, func):
    with open(f"inputs/input_{letter}.txt") as file:
        lines = file.read().split("\n")
    outputs = []
    print(f"------ Challenge {letter.upper()} ------")
    for line in lines:
        n, k = [int(n) for n in line.split()]
        outputs.append(func(n, k))
    return outputs


def boolean_output(letter: str, outputs: List[bool]):
    with open(f"outputs/{letter}.txt", "w") as file:
        for output in outputs:
            if output:
                file.write("T")
            else:
                file.write("F")


def integer_output(letter, outputs):
    s_outputs = [str(n) for n in outputs]
    with open(f"outputs/{letter}.txt", "w") as file:
        file.write("\n".join(s_outputs))


def grid_output(letter, grids):
    with open(f"outputs/{letter}.txt", "w") as file:
        file.write("\n\n".join(["\n".join(["".join(row) for row in grid]) for grid in grids]))


def part_a1():
    outputs = grid_input("a1", chain)
    boolean_output("a1", outputs)


def part_a2():
    outputs = grid_input("a2", tic_tac_toe)
    boolean_output("a2", outputs)


def part_b1():
    outputs = grid_input("b1", max_chain)
    integer_output("b1", outputs)


def part_b2():
    outputs = integer_input("b2", tic_tac_no)
    integer_output("b2", outputs)


def part_b3():
    outputs = two_integer_input("b3", chain_blocker)
    grid_output("b3", outputs)


part_a1()
part_a2()
part_b1()
part_b2()
part_b3()
