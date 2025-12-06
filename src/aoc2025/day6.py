"""Day 6 solution to AoC 2025"""

import re
from typing import Literal, cast

type Operator = Literal["*", "+"]
type Sheet = list[list[int]]

type PuzzleInput = tuple[Sheet, list[Operator]]

SAMPLE_INPUT_STR = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

SAMPLE_INPUT: PuzzleInput = (
    [[123, 328, 51, 64], [45, 64, 387, 23], [6, 98, 215, 314]],
    ["*", "+", "*", "+"],
)


def solution1(puzzle_input) -> int:
    """Solve day6 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day6 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> PuzzleInput:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    lines = puzzle_input.splitlines()
    single_spaced_lines = [re.sub(r" +", " ", line) for line in lines]
    trimmed = [line.strip() for line in single_spaced_lines]
    *num_strlist, operators = trimmed
    numbers: Sheet = [[int(i) for i in line.split()] for line in num_strlist]
    return numbers, [cast(Operator, op) for op in operators.split()]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day6 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day6 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
