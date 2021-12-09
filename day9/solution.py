from os.path import exists

def main():
    print("[DAY 9]")

    puzzle_input = []

    if exists("day9/input.txt"):
        f = open("day9/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    for line in f:
        puzzle_input.append(line.strip())

    def calculate_risk_level():
        width = len(puzzle_input[0])
        height = len(puzzle_input)
        risk_level_sum = 0
        bottom_basins = []

        for i in range(width):
            for v in range(height):
                checks = []

                if i != 0:
                    checks.append(puzzle_input[v][i - 1])
                if i != width - 1:
                    checks.append(puzzle_input[v][i + 1])
                if v != 0:
                    checks.append(puzzle_input[v - 1][i])
                if v != height - 1:
                    checks.append(puzzle_input[v + 1][i])

                is_lowest = True
                for check in checks:
                    if check <= puzzle_input[v][i]:
                        is_lowest = False
                        
                if is_lowest:
                    risk_level_sum += int(puzzle_input[v][i]) + 1
                    bottom_basins.append([i, v])
            
        return (risk_level_sum, bottom_basins)

    def calculate_basin(positions, new_positions):
        width = len(puzzle_input[0])
        height = len(puzzle_input)

        next_new_positions = []
        for new_pos in new_positions:
            if new_pos[0] != 0 and puzzle_input[new_pos[1]][new_pos[0] - 1] != '9' and [new_pos[0] - 1, new_pos[1]] not in positions:
                next_new_positions.append([new_pos[0] - 1, new_pos[1]])
                positions.append([new_pos[0] - 1, new_pos[1]])
            if new_pos[0] != width - 1 and puzzle_input[new_pos[1]][new_pos[0] + 1] != '9' and [new_pos[0] + 1, new_pos[1]] not in positions:
                next_new_positions.append([new_pos[0] + 1, new_pos[1]])
                positions.append([new_pos[0] + 1, new_pos[1]])
            if new_pos[1] != 0 and puzzle_input[new_pos[1] - 1][new_pos[0]] != '9' and [new_pos[0], new_pos[1] - 1] not in positions:
                next_new_positions.append([new_pos[0], new_pos[1] - 1])
                positions.append([new_pos[0], new_pos[1] - 1])
            if new_pos[1] != height - 1 and puzzle_input[new_pos[1] + 1][new_pos[0]] != '9' and [new_pos[0], new_pos[1] + 1] not in positions:
                next_new_positions.append([new_pos[0], new_pos[1] + 1])
                positions.append([new_pos[0], new_pos[1] + 1])

        if len(next_new_positions) == 0:
            return len(positions)
        else:
            return calculate_basin(positions, next_new_positions)

    def calculate_top_basins():
        basin_sizes = []
        basin_positions = calculate_risk_level()[1]

        for basin_position in basin_positions:
            basin_sizes.append(calculate_basin([[basin_position[0], basin_position[1]]], [[basin_position[0], basin_position[1]]]))
        
        basin_sizes = sorted(basin_sizes, reverse=True)

        return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
                    

    print("[TASK 1]: " + str(calculate_risk_level()[0]))

    print("[TASK 2]: " + str(calculate_top_basins()))

if __name__ == "__main__":
    main()
