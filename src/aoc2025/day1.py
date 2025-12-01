"""Day 1 solution to AoC 2025"""

type Instruction = int
"""A single, signed instruction like +51 = R51"""


SAMPLE_INPUT_STR = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

SAMPLE_INPUT = [-68, -30, +48, -5, +60, -55, -1, -99, +14, -82]


def solution1(puzzle_input: list[Instruction]) -> int:
    """Solve day1 part 1

    >>> solution1(SAMPLE_INPUT)
    3
    """
    position = 50
    acc = 0
    for movement in puzzle_input:
        position = (position + movement) % 100
        if position == 0:
            acc += 1
    return acc


def solution2(puzzle_input: list[Instruction]) -> int:
    """Solve day1 part 2

    >>> solution2([+1000])
    10
    >>> solution2(SAMPLE_INPUT)
    6
    """
    position = 50
    acc = 0
    for movement in puzzle_input:
        # Process each tick of movements
        unit = 1 if movement > 0 else -1
        for _ in range(abs(movement)):
            position += unit
            if position == 100:  # Cycle up
                position = 0
            if position == 0:
                acc += 1
            if position < 0:  # Cycle down
                position = 99
    return acc


def read_puzzle_input(puzzle_input: str) -> list[Instruction]:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    lines = puzzle_input.splitlines(keepends=False)
    acc: list[int] = []
    for line in lines:
        direction, distance = line[0], int(line[1:])
        match direction:
            case "L":
                acc.append(-distance)
            case "R":
                acc.append(+distance)
    return acc


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
