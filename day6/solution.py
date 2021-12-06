from os.path import exists

def main():
    print("[DAY 6]")

    if exists("day6/input.txt"):
        f = open("day6/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    puzzle_input = list(map(int, f.readline().strip().split(',')))
    f.close()

    # This way is much quicker than a nested loop as it has a complexity of O(n)
    def quick_find_fish(days):
        fish_stages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for fish in puzzle_input:
            fish_stages[fish] += 1
        fish_stages = list(fish_stages.values())

        for _ in range(days):
            fish_stages_zero = fish_stages[0]
            fish_stages = fish_stages[1:] + fish_stages[:1]
            fish_stages[6] += fish_stages_zero

        return sum(fish_stages)

    print("[TASK 1]: " + str(quick_find_fish(80)))

    print("[TASK 2]: " + str(quick_find_fish(256)))

if __name__ == "__main__":
    main()
