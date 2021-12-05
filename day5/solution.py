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

    grid = [[0] * 10] * 10

    def unit(number):
        if number < 0:
            return -1
        else: return 1

    def calculate_line_straigt(vent_line, the_grid):
        index_difference = 0
        if vent_line[1] == vent_line[3]:
            index_difference = 1

        difference = int(vent_line[1 - index_difference]) - int(vent_line[3 - index_difference])
        if abs(difference) < 15:
            print(vent_line)
            print(difference)
        for i in range(0, abs(difference) + 1):
            # if index_difference == 1:
            print(int(vent_line[2]) + (i * unit(difference)), int(vent_line[1]))
            print(the_grid[int(vent_line[2]) + (i * unit(difference))][int(vent_line[1])] + 1)
            the_grid[int(vent_line[2]) + (i * unit(difference))][int(vent_line[1])] += 1
            # else:
            #     if abs(difference) < 15:
            #         print(the_grid[int(vent_line[0])][int(vent_line[3]) + (i * unit(difference))] + 1)
            #     the_grid[int(vent_line[0])][int(vent_line[3]) + (i * unit(difference))] += 1

    # for vent_line in puzzle_input:
    #     if vent_line[0] == vent_line[2] or vent_line[1] == vent_line[3]:
    #         calculate_line_straigt(vent_line)

    vent_line = puzzle_input[0]
    if vent_line[0] == vent_line[2] or vent_line[1] == vent_line[3]:
        calculate_line_straigt(vent_line, grid)
            
    dangerous_positions = 0

    print('\n'.join(' '.join(str(x) for x in row) for row in grid))

    for i in grid:
        for v in i:
            if v >= 2:
                dangerous_positions += 1

    # 972027
    # 971028
    # 971028

    print("[TASK 1]: " + str(dangerous_positions))

    # print("[TASK 1]: " + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

    # print("[TASK 2]: " + str(findListValue(puzzle_input, True, 0) * findListValue(puzzle_input, False, 0)))

if __name__ == "__main__":
    main()
