"""Day 6 solution to AoC 2025"""

import re
from typing import Any, Literal, cast

import numpy as np

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

# np.add, np.mul aren't JUST Callables, as we use their .reduce() method
# So use ANY type as shortcut, cannae be bothered
OP_MAP: dict[Operator, Any] = {"*": np.multiply, "+": np.add}


def solution1(puzzle_input: PuzzleInput) -> int:
    """Solve day6 part 1, but also part 2 when data processed

    >>> solution1(SAMPLE_INPUT)
    4277556
    >>> solution1(rtl_read_sheet(SAMPLE_INPUT_STR))
    3263827
    """
    acc = 0
    sheet, operators = puzzle_input
    grid = np.array(sheet, dtype=int)
    # Along the rows (remember Numpy's array-addressing)
    for i in range(grid.shape[1]):
        # Reduce by that operator
        op_func = OP_MAP[operators[i]]
        acc += int(op_func.reduce(grid[:, i]))
    return acc


def rtl_read_sheet(puzzle_input: str) -> PuzzleInput:
    """Read the given sheet in right to left format, per part 2

    >>> rtl_read_sheet(SAMPLE_INPUT_STR)[0]
    [[4, 175, 8, 356], [431, 581, 248, 24], [623, 32, 369, 1]]
    """
    *num_strlist, operators = puzzle_input.splitlines()
    width = max(len(line) for line in num_strlist)
    padded = [list(line.ljust(width)) for line in num_strlist]
    grid = np.array(padded, dtype="U1")
    flipped = np.transpose(grid)[::-1, :]  # full char line = number
    operators_trimmed = re.sub(r" +", " ", operators).strip()
    ops = [cast(Operator, op) for op in operators_trimmed.split(" ")]
    sheet: Sheet = []
    line: list[int] = []
    for i in range(width):
        number_str = "".join(flipped[i]).strip()
        if not number_str:  # Empty line = separator for new problem
            sheet.append(line)
            line = []
            continue
        # Line has number: append
        line.append(int(number_str))
    # Last line won't have a separator: take manually
    sheet.append(line)
    # Last second transposition:
    grid = np.transpose(np.array(sheet, dtype=int))
    return grid.tolist(), ops[::-1]


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
    return solution1(rtl_read_sheet(puzzle_input))
