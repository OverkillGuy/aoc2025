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

    Raises:
        ValueError: When memory footprint > 1GiB (max of range-end > 1e12)

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


def solution2_expand(puzzle_input: PuzzleInput) -> int:
    """Solve day5 part 2 via PROHIBITIVE MEMORY-HUNGRY SOLUTION.

    Solved by expanding ALL ranges into a "map of covered ids" as bool-array.
    This way we unroll range 1-3 to tick to True ids 1, 2, and 3.
    Repeat coverage flips True to still True, dealing with overlaps.
    No need to deal with ordering of ranges either, as all will be covered.

    We just need to count the resulting range, once expanded as a "list of ids"

    >>> solution2(SAMPLE_INPUT)
    14

    Raises:
        ValueError: When memory footprint > 1GiB (max of range-end > 1e12)
    """
    return sum(expand(puzzle_input[0]))


def merge(ranges: list[Range]) -> list[Range]:
    """Merge given intervals via sorted comparisons

    Overlaps merged:
    >>> merge([(1, 3), (2, 5)])
    [(1, 5)]

    Same start/end merged too:
    >>> merge([(1, 3), (3, 5)])
    [(1, 5)]

    Adjacent ranges merged:
    >>> merge([(1, 2), (3, 6)])
    [(1, 6)]

    Individual ranges allowed, let alone:
    >>> merge([(1, 1), (4, 4)])
    [(1, 1), (4, 4)]
    """
    sorted_ranges = sorted(ranges, key=lambda range: range[0])
    acc = []
    s0, e0 = sorted_ranges.pop(0)
    while sorted_ranges:
        s1, e1 = sorted_ranges.pop(0)
        # Overlap / Adjacent: Collapse, taking biggest
        if s1 <= e0 + 1:
            e0 = max(e0, e1)
        else:
            # Not adjacent: collect the interval 0, ratchet up interval
            acc.append((s0, e0))
            s0, e0 = s1, e1
    # Pick last remaining interval too
    return acc + [(s0, e0)]


def count_range(ranges: list[Range]) -> int:
    """Count how many numbers are there in a given list of ranges

    >>> count_range(merge(SAMPLE_INPUT[0]))
    14
    """
    return sum([end - start + 1 for start, end in ranges])


def solution2(puzzle_input: PuzzleInput) -> int:
    """Solve day 5 part 2, using proper sorted interval merging

    >>> solution2(SAMPLE_INPUT)
    14
    """
    return count_range(merge(puzzle_input[0]))


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
