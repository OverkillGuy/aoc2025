"""Day 4 solution to AoC 2025"""

type Grid = list[list[bool]]
"""A 2D grid of bools (True if is a roll)"""

SAMPLE_INPUT_STR = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


SAMPLE_INPUT: Grid = [
    [False, False, True, True, False, True, True, True, True, False],
    [True, True, True, False, True, False, True, False, True, True],
    [True, True, True, True, True, False, True, False, True, True],
    [True, False, True, True, True, True, False, False, True, False],
    [True, True, False, True, True, True, True, False, True, True],
    [False, True, True, True, True, True, True, True, False, True],
    [False, True, False, True, False, True, False, True, True, True],
    [True, False, True, True, True, False, True, True, True, True],
    [False, True, True, True, True, True, True, True, True, False],
    [True, False, True, False, True, True, True, False, True, False],
]


def solution1(puzzle_input) -> int:
    """Solve day4 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day4 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> Grid:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    lines = [list(line) for line in puzzle_input.splitlines()]
    return [[c == "@" for c in line] for line in lines]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
