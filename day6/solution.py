from os.path import exists

def main():
    print("[DAY 6]")

    puzzle_input = []

    if exists("day6/input.txt"):
        f = open("day6/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    puzzle_input = f.readline().strip().split(',')
    f.close()

    # print("[TASK 1]: " + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

    # print("[TASK 2]: " + str(findListValue(puzzle_input, True, 0) * findListValue(puzzle_input, False, 0)))

if __name__ == "__main__":
    main()
