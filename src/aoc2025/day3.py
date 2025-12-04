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


def max2_joltage(batteries: Bank) -> int:
    """Compute the maximum joltage for a given bank using 2 batteries

    >>> [max2_joltage(i) for i in SAMPLE_INPUT]
    [98, 89, 78, 92]
    """
    joltages = list(batteries)
    max_digit = max(joltages[:-1])  # Leave out last digit
    first_max_digit_index = joltages.index(max_digit)
    second_max_digit = max(joltages[first_max_digit_index + 1 :])
    top2_digits = max_digit + second_max_digit
    return int("".join(top2_digits))


def solution1(puzzle_input: list[Bank]) -> int:
    """Solve day3 part 1

    >>> solution1(SAMPLE_INPUT)
    357
    """
    return sum(max2_joltage(bank) for bank in puzzle_input)


def maxn_joltage(batteries: Bank, n: int) -> int:
    """Compute the maximum joltage for a given bank, generalized for n batteries

    Iterate the search the maximum of interval [idx+1: - (n - i - 1)] in general

    But on the edge boundaries of the list (i = 0 and i = n - 1)
    we address the range differently to express "take all of the edge".

    >>> [maxn_joltage(i, 12) for i in SAMPLE_INPUT]
    [987654321111, 811111111119, 434234234278, 888911112111]
    """
    joltages = list(batteries)
    top_digits = []
    idx = -1  # Want to start range at l[0:], but since l[idx+1:], set idx = -1
    for i in range(0, n):
        start_range = idx + 1
        # When searching i-th joltage, leave out the right most digits for later
        end_range = -(n - i - 1)
        if i + 1 == n:  # But at the end, take ALL:
            # Cannot express l[:], because l[:-0] fails, so we go for l[:len(l)]
            end_range = len(joltages)
        pick_range = joltages[start_range:end_range]
        max_digit = max(pick_range)
        top_digits.append(max_digit)
        # Pick from the real joltages (using real offsets, not from pick_range!)
        idx = batteries.index(max_digit, start_range, end_range)
    return int("".join(top_digits))


def solution2(puzzle_input: list[Bank]) -> int:
    """Solve day3 part 2

    >>> solution2(SAMPLE_INPUT)
    3121910778619
    """
    return sum(maxn_joltage(bank, 12) for bank in puzzle_input)


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
