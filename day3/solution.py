from os.path import exists

def main():
    print("[DAY 3]")

    puzzle_input = []

    if exists("day3/input.txt"):
        f = open("day3/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    for line in f:
        puzzle_input.append(line)

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(12):
        ones = 0
        zeros = 0
        for line in puzzle_input:
            if line[i] == "1":
                ones += 1
            elif line[i] == "0":
                zeros += 1
            else:
                return print(f"[TASK 1]: An Error Has Occured")
        if ones > zeros:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print("[TASK 1]: " + str(int(gamma_rate, 2) * int(epsilon_rate, 2)))

    def findListValue(new_list, largest, index):
        if len(new_list) == 1:
            return int(new_list[0], 2)
        ones = []
        zeros = []
        for line in new_list:
            if line[index] == "1":
                ones.append(line)
            elif line[index] == "0":
                zeros.append(line)
            else:
                return print(f"[TASK 2]: An Error Has Occured")
                
        if (largest or len(ones) >= len(zeros)) and not (largest and len(ones) >= len(zeros)):
            return findListValue(ones[:], largest, index + 1)
        else:
            return findListValue(zeros[:], largest, index + 1)

    print("[TASK 2]: " + str(findListValue(puzzle_input, True, 0) * findListValue(puzzle_input, False, 0)))

if __name__ == "__main__":
    main()
