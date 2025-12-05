"""Day 4 solution to AoC 2025"""

import numpy as np
from numpy.typing import NDArray
from scipy.signal import convolve

type Grid = NDArray[bool]

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


SAMPLE_INPUT: Grid = np.array(
    [
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
    ],
    dtype=bool,
)


def count8(grid: Grid) -> Grid:
    """Count the number of 8-neighbours

    >>> impulse = np.zeros((3, 3))
    >>> impulse[1, 1] = 1
    >>> reverse = 1 - impulse
    >>> bool((count8(impulse) == reverse).all())
    True
    """
    padded = np.pad(grid, pad_width=1, mode="constant", constant_values=False)
    kernel = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    count8 = convolve(padded, np.array(kernel), mode="same")
    return count8[1:-1, 1:-1]


def find_reachable_rolls(g: Grid) -> Grid:
    """Find reachable rolls"""
    count8_under4 = count8(g) < 4
    return count8_under4 & g


def count_array(g: Grid) -> int:
    """Count the number of items that are True"""
    return int(np.sum(g))


def solution1(puzzle_input: Grid) -> int:
    """Solve day4 part 1

    >>> solution1(SAMPLE_INPUT)
    13
    """
    reachable_rolls = find_reachable_rolls(puzzle_input)
    return count_array(reachable_rolls)


def iterate(g: Grid) -> tuple[Grid, int]:
    """Find reachable, and iterate"""
    reachable = find_reachable_rolls(g)
    now_reachable = g & (~reachable)  # Remove reachables (X AND (NOT TRUE))
    return now_reachable, count_array(reachable)


def solution2(puzzle_input: Grid) -> int:
    """Solve day4 part 2

    >>> solution2(SAMPLE_INPUT)
    43
    """
    old_grid = np.zeros_like(puzzle_input, dtype=bool)
    new_grid = puzzle_input
    acc = 0
    while not ((new_grid == old_grid).all()):  # Until we're done changing
        old_grid = new_grid
        new_grid, count = iterate(old_grid)
        acc += count
    return acc


def read_puzzle_input(puzzle_input: str) -> Grid:
    """Process the puzzle input string

    >>> bool((read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT).all())
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
