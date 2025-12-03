"""Day 3 solution to AoC 2025"""

type Bank = str
"""A single "Battery Bank" = line of numbers"""

SAMPLE_INPUT_STR = """987654321111111
811111111111119
234234234234278
818181911112111
"""

SAMPLE_INPUT: list[Bank] = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def solution1(puzzle_input: list[Bank]) -> int:
    """Solve day3 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day3 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> list[Bank]:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    return puzzle_input.splitlines()


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
