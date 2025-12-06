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


def is_fresh(ingredient: int, freshs: FreshRanges) -> bool:
    """Checks if given ingredient is fresh

    >>> [is_fresh(i, SAMPLE_INPUT[0]) for i in SAMPLE_INPUT[1]]
    [False, True, False, True, True, False]
    """
    for start, end in freshs:
        if start <= ingredient <= end:
            return True
    return False


def solution1(puzzle_input: PuzzleInput) -> int:
    """Solve day5 part 1

    >>> solution1(SAMPLE_INPUT)
    3
    """
    fresh, available = puzzle_input
    return sum(is_fresh(item, fresh) for item in available)


def expand(ranges: list[Range]) -> list[bool]:
    """Expand the ranges of which ids are covered, to a list of covered-ness

    Index +1, maps back to the id being checked.

    NOTE: Uses, returns O(N) in memory, N = max(all ranges' end-value) in bits.
    This is obviously prohibitive when N >> 1e12 = Gigabytes range!

    For that reason, throws a ValueError when N > 1e12.


    >>> expand([(1, 3), (2, 5)])
    [True, True, True, True, True]
    >>> expand([(1, 2), (4, 5)])
    [True, True, False, True, True]
    >>> expand([(1, 2), (4, 6)])
    [True, True, False, True, True, True]
    >>> expand([(1, 1), (4, 4)])
    [True, False, False, True]

    """
    max_range = max([end for _start, end in ranges])
    if max_range > 1e12:
        raise ValueError("Aborting as memory required would exceed 1GiB")
    ids = [False for _ in range(max_range)]
    for start, end in ranges:
        expanded = list(range(start - 1, end))  # Move to 0-indexing via N-1
        for i in expanded:
            ids[i] = True
    return ids




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
