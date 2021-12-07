from os.path import exists
import math

def main():
    print("[DAY 7]")

    puzzle_input = []

    if exists("day7/input.txt"):
        f = open("day7/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    puzzle_input = list(map(int, f.readline().strip().split(',')))

    def calculate_fuel_cost_1(puzzle_input):
        fuel_cost = math.inf
        for position in range(max(puzzle_input) + 1):
            temp_fuel_cost = 0
            for crab in puzzle_input:
                temp_fuel_cost += abs(crab - position)
            if temp_fuel_cost < fuel_cost:
                fuel_cost = temp_fuel_cost
        return fuel_cost

    def calculate_crap_fuel(distance):
        return (distance ** 2 + distance) / 2

    def calculate_fuel_cost_2(puzzle_input):
        fuel_cost = math.inf
        for position in range(max(puzzle_input) + 1):
            temp_fuel_cost = 0
            for crab in puzzle_input:
                temp_fuel_cost += calculate_crap_fuel(abs(crab - position))
            if temp_fuel_cost < fuel_cost:
                fuel_cost = temp_fuel_cost
        return int(fuel_cost)

    print("[TASK 1]: " + str(calculate_fuel_cost_1(puzzle_input)))

    print("[TASK 2]: " + str(calculate_fuel_cost_2(puzzle_input)))

if __name__ == "__main__":
    main()
