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


def max_joltage(batteries: Bank) -> int:
    """Compute the maximum joltage for a given bank

    >>> [max_joltage(i) for i in SAMPLE_INPUT]
    [98, 89, 78, 92]
    """
    joltages = list(batteries)
    max_digit = max(joltages[:-1])  # Leave out last digit
    first_max_digit_index = joltages.index(max_digit)
    second_max_digit = max(joltages[first_max_digit_index + 1 :])
    top2_digits = max_digit + second_max_digit
    return int("".join(top2_digits))


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
