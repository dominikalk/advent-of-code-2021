from day1.solution import main as day1_solution
from day2.solution import main as day2_solution
from day3.solution import main as day3_solution
from day4.solution import main as day4_solution
from day5.solution import main as day5_solution
from day6.solution import main as day6_solution
from day7.solution import main as day7_solution
from day8.solution import main as day8_solution



def main():
    day_solutions = [day1_solution, day2_solution, day3_solution, day4_solution, day5_solution, day6_solution, day7_solution, day8_solution]
    days_completed = len(day_solutions)
    day_input = input(f"Which day would you like the solution to? (1 - {days_completed} else ALL): ")
    if not day_input.isnumeric() or int(day_input) < 1 or int(day_input) > days_completed:
        for day_solution in day_solutions:
            day_solution()
    else:
        day_solutions[int(day_input) - 1]()

if __name__ == "__main__":
    main()