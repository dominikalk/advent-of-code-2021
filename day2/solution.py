puzzle_input = []

f = open("input.txt", "r")
for line in f:
    puzzle_input.append(line)

f.close()

position = 0
depth = 0

for move in puzzle_input:
    split_move = move.split()
    if split_move[0] == 'forward':
        position += int(split_move[1])
    elif split_move[0] == 'down':
        depth += int(split_move[1])
    elif split_move[0] == 'up':
        depth -= int(split_move[1])
    else:
        print('An Error Has Occured')
        break

print("Task 1: Position: ", position, ", Depth: ", depth, ", Multiplication: ", position * depth)

position2 = 0
depth2 = 0
aim2 = 0

for move in puzzle_input:
    split_move = move.split()
    if split_move[0] == 'forward':
        position2 += int(split_move[1])
        depth2 += aim2 * int(split_move[1])
    elif split_move[0] == 'down':
        aim2 += int(split_move[1])
    elif split_move[0] == 'up':
        aim2 -= int(split_move[1])
    else:
        print('An Error Has Occured')
        break

print("Task 2: Position: ", position2, ", Depth: ", depth2, ", Multiplication: ", position2 * depth2)
