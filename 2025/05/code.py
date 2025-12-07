import pathlib

data = pathlib.Path("2025/05/input.txt").read_text(encoding="utf-8")

id_ranges = [list(line) for line in data.split("\n")]
print(id_ranges)