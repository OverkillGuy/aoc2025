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


def range_filter_invalid(product_range: Range) -> list[int]:
    """Filter the invalid IDs in a given range

    >>> [range_filter_invalid(i) for i in SAMPLE_INPUT[:5]]
    [[11, 22], [99], [1010], [1188511885], [222222]]
    >>> [range_filter_invalid(i) for i in SAMPLE_INPUT[5:]]
    [[], [446446], [38593859], [], [], []]
    """
    start, end = product_range
    return [i for i in range(start, end + 1) if is_invalid(i)]


def solution1(puzzle_input: list[Range]) -> int:
    """Solve day2 part 1

    >>> solution1(SAMPLE_INPUT)
    1227775554
    """
    return sum(sum(range_filter_invalid(range)) for range in puzzle_input)


def is_invalid_part2(product_id: int) -> bool:
    """Check if a product_id is invalid per part2

    >>> [is_invalid_part2(i) for i in [11, 22, 99, 111, 999, 1010, 1188511885, 222222]]
    [True, True, True, True, True, True, True, True]
    >>> [is_invalid_part2(i) for i in [446446, 38593859, 5656, 824824824, 2121212121]]
    [True, True, True, True, True]
    >>> is_invalid_part2(11211)
    False
    >>> [is_invalid_part2(i) for i in [11, 111, 11111]]
    [True, True, True]
    """
    id_str = str(product_id)
    num_digits = len(id_str)
    half = num_digits // 2
    # Try checking str against repeated first chars for 1, 2, up to half
    for ngram_size in range(1, half + 1):
        if num_digits % ngram_size != 0:
            continue  # Generalized "odd cannot be repeating": 1112111, n % 3 != 0
        # Generate the fully repeating pattern from prefix, for that ngram_size
        num_repeat = num_digits // ngram_size
        ngram_prefix = id_str[:ngram_size]
        full_repeat = "".join(ngram_prefix * num_repeat)
        if id_str == full_repeat:
            return True
    return False


def range_filter_invalid_part2(product_range: Range) -> list[int]:
    """Filter the invalid IDs in a given range, for part 2

    >>> [range_filter_invalid_part2(i) for i in SAMPLE_INPUT[:5]]
    [[11, 22], [99, 111], [999, 1010], [1188511885], [222222]]
    >>> [range_filter_invalid_part2(i) for i in SAMPLE_INPUT[5:]]
    [[], [446446], [38593859], [565656], [824824824], [2121212121]]
    """
    start, end = product_range
    return [i for i in range(start, end + 1) if is_invalid_part2(i)]


def solution2(puzzle_input: list[Range]) -> int:
    """Solve day2 part 2

    >>> solution2(SAMPLE_INPUT)
    4174379265
    """
    return sum(sum(range_filter_invalid_part2(range)) for range in puzzle_input)


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
