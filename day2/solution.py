from os.path import exists

def main():
    print("[DAY 2]")

    puzzle_input = []

    if exists("day2/input.txt"):
        f = open("day2/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    for line in f:
        puzzle_input.append(line)

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
            return print('[TASK 1]: An Error Has Occured')

    print("[TASK 1]: " + str(position * depth))

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
            return print('[TASK 2]: An Error Has Occured')

    print("[TASK 2]: " + str(position2 * depth2))

if __name__ == "__main__":
    main()
