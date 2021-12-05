from os import confstr
from os.path import exists

def main():
    print("[DAY 5]")

    puzzle_input = []

    if exists("day5/input.txt"):
        f = open("day5/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    for line in f:
        puzzle_input.append(line.strip().replace(' -> ', ',').split(","))

    grid = [[0] * 999 for _ in range(999)]

    def unit(number):
        if number < 0:
            return -1
        else: return 1

    def calculate_line_straigt(vent_line, the_grid):
        index_difference = 0
        if vent_line[1] == vent_line[3]:
            index_difference = 1

        difference = int(vent_line[1 - index_difference]) - int(vent_line[3 - index_difference])
        for i in range(0, abs(difference) + 1):
            if index_difference == 1:
                the_grid[int(vent_line[1])][int(vent_line[2]) + (i * unit(difference))] += 1
            else:
                the_grid[int(vent_line[3]) + (i * unit(difference))][int(vent_line[0])] += 1

    for vent_line in puzzle_input:
        if vent_line[0] == vent_line[2] or vent_line[1] == vent_line[3]:
            calculate_line_straigt(vent_line, grid)
            
    dangerous_positions = sum([1 if x > 1 else 0 for x in [j for sub in grid for j in sub]])

    print("[TASK 1]: " + str(dangerous_positions))

    def calculate_line_diagonal(vent_line, the_grid):
        x_difference = int(vent_line[0]) - int(vent_line[2])
        y_difference = int(vent_line[1]) - int(vent_line[3])

        for i in range(0, abs(x_difference) + 1):
            the_grid[int(vent_line[3]) + (i * unit(y_difference))][int(vent_line[2]) + (i * unit(x_difference))] += 1

    for vent_line in puzzle_input:
        if vent_line[0] != vent_line[2] and vent_line[1] != vent_line[3]:
            calculate_line_diagonal(vent_line, grid)

    dangerous_positions = sum([1 if x > 1 else 0 for x in [j for sub in grid for j in sub]])

    print("[TASK 2]: " + str(dangerous_positions))

if __name__ == "__main__":
    main()
