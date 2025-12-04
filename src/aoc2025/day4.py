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


def solution1(puzzle_input) -> int:
    """Solve day4 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day4 part 2"""
    return 0


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
