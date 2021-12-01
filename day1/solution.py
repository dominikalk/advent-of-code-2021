puzzle_input = []

f = open("input.txt", "r")
for line in f:
    puzzle_input.append(line)

f.close()

increased_task_1 = 0

for i in range(len(puzzle_input)):
    if i != 0 and int(puzzle_input[i]) > int(puzzle_input[i - 1]):
        increased_task_1 += 1

print(increased_task_1)

increased_task_2 = 0

def calculate_value(index, the_puzzle_input):
    return int(the_puzzle_input[index]) + int(the_puzzle_input[index + 1]) + int(the_puzzle_input[index + 2])

for i in range(len(puzzle_input) - 2):
    if i != 0 and calculate_value(i, puzzle_input) > calculate_value(i - 1, puzzle_input):
            increased_task_2 += 1

print(increased_task_2)