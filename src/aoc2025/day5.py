"""Day 5 solution to AoC 2025"""

type Range = tuple[int, int]
type FreshRanges = list[Range]
type AvailableList = list[int]
type PuzzleInput = tuple[FreshRanges, AvailableList]


SAMPLE_INPUT_STR = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

SAMPLE_INPUT: PuzzleInput = (
    [
        (3, 5),
        (10, 14),
        (16, 20),
        (12, 18),
    ],
    [1, 5, 8, 11, 17, 32],
)


def solution1(puzzle_input) -> int:
    """Solve day5 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day5 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> PuzzleInput:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    fresh_str, available_str = puzzle_input.split("\n\n")
    fresh_list = [line.split("-") for line in fresh_str.splitlines()]
    fresh = [(int(i), int(j)) for i, j in fresh_list]
    available = [int(line) for line in available_str.splitlines()]
    return fresh, available


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
