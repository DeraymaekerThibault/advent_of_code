import pathlib

def is_divisible_by_repdigit(number: int) -> bool:
    """Check if number is divisible by a repdigit (11, 101, 1001, etc.)."""
    seq = str(number)
    if len(seq) % 2 != 0:
        return False
    k = len(seq) // 2
    divisor = 10**k + 1
    return number % divisor == 0

def has_repeated_sequence(number: int) -> bool:
    """Check if the string representation contains itself as a substring."""
    seq = str(number)
    return len(seq) > 1 and seq in (seq + seq)[1:-1]

def process_ranges(ranges: list[tuple[int, int]], predicate) -> int:
    """Sum numbers in ranges that satisfy the predicate."""
    total = 0
    for start, end in ranges:
        for number in range(max(1, start), end + 1):
            if predicate(number):
                total += number
    return total

# Parse input
data = pathlib.Path("2025/02/input.txt").read_text(encoding="utf-8")
ranges = [tuple(map(int, r.split("-"))) for r in data.strip().split(",")]

# Calculate results
sum_wrong_ids_1 = process_ranges(ranges, is_divisible_by_repdigit)
sum_wrong_ids_2 = process_ranges(ranges, has_repeated_sequence)

print("Sum of wrong IDs:", sum_wrong_ids_1)
print("Sum of wrong IDs with repeated sequence:", sum_wrong_ids_2)