import pathlib

data = pathlib.Path("2025/01/input.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

start_position_1 = 50
start_position_2 = 50
solution_1 = 0
solution_2 = 0

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == "R":
        start_position_1 = (start_position_1 + amount) % 100
    else:  
        start_position_1 = (start_position_1 - amount % 100) % 100

    if start_position_1 == 0:
        solution_1 += 1

    direction_offset = 1 if direction == "R" else -1
    for _ in range(amount):
        start_position_2 = (start_position_2 + direction_offset) % 100
        if start_position_2 == 0:
            solution_2 += 1

print("Solution1:", solution_1)
print("Solution2:", solution_2)
