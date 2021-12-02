from os.path import exists

def main():
    print("[DAY 1]")

    puzzle_input = []

    if exists("day1/input.txt"):
        f = open("day1/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("Could Not Find Input")
    for line in f:
        puzzle_input.append(line)
    f.close()

    increased_task_1 = 0

    for i in range(len(puzzle_input)):
        if i != 0 and int(puzzle_input[i]) > int(puzzle_input[i - 1]):
            increased_task_1 += 1

    print("[TASK 1]: " + str(increased_task_1))

    increased_task_2 = 0

    def calculate_value(index, the_puzzle_input):
        return int(the_puzzle_input[index]) + int(the_puzzle_input[index + 1]) + int(the_puzzle_input[index + 2])

    for i in range(len(puzzle_input) - 2):
        if i != 0 and calculate_value(i, puzzle_input) > calculate_value(i - 1, puzzle_input):
                increased_task_2 += 1

    print("[TASK 2]: " + str(increased_task_2))

if __name__ == "__main__":
    main()