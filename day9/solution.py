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
            
        return risk_level_sum

    print("[TASK 1]: " + str(calculate_risk_level()))

    # print("[TASK 2]: " + str(calculate_output_addition()))

if __name__ == "__main__":
    main()
