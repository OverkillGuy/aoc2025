"""Day 2 solution to AoC 2025"""

type Range = tuple[int, int]


SAMPLE_INPUT_STR = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

SAMPLE_INPUT: list[Range] = [
    (11, 22),
    (95, 115),
    (998, 1012),
    (1188511880, 1188511890),
    (222220, 222224),
    (1698522, 1698528),
    (446443, 446449),
    (38593856, 38593862),
    (565653, 565659),
    (824824821, 824824827),
    (2121212118, 2121212124),
]


def is_invalid(product_id: int) -> bool:
    """Check if a product_id is invalid

    >>> [is_invalid(i) for i in [11, 22, 99, 1010, 1188511885]]
    [True, True, True, True, True]
    >>> is_invalid(11211)
    False
    """
    id_str = str(product_id)
    num_digits = len(id_str)
    if num_digits % 2 == 1:
        return False
    half = num_digits // 2
    first_half, second_half = id_str[:half], id_str[half:]
    return first_half == second_half


def solution1(puzzle_input) -> int:
    """Solve day2 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day2 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> list[Range]:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    ranges_str = puzzle_input.split(",")
    ranges_split = [item.split("-") for item in ranges_str]
    return [(int(i), int(j)) for (i, j) in ranges_split]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
