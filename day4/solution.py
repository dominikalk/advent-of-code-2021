from os.path import exists

def main():
    print("[DAY 4]")

    puzzle_numbers = []
    puzzle_boards = []

    if exists("day4/input.txt"):
        f = open("day4/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    board_number = 0
    current_board = []
    for i, line in enumerate(f):
        if i == 0:
            puzzle_numbers = line.strip().split(',')
        elif line.strip() != '':
            # every new board starts on the line 6n - 3
            if 6 * (board_number + 1) - 3 == i + 1:
                board_number += 1
                if len(current_board) != 0:
                    puzzle_boards.append(current_board)
                    current_board = []
            
            current_board.append(line.strip().split())

    def calculate_board(board):
        """Takes in a board and returns the score of the board and the number of moves it took"""
        # first 5 are columns, second 5 are rows
        hasWon = False
        buckets = [0] * 10
        unused_numbers = [j for sub in board for j in sub]
        moves = 0
        for number in puzzle_numbers:
            moves += 1
            for i, row in enumerate(board):
                for v, row_number in enumerate(row):
                    if row_number == number:
                        unused_numbers.remove(number)
                        buckets[v] += 1
                        buckets[i + 5] += 1
                        if buckets[v] == 5 or buckets[i + 5] == 5:
                            hasWon = True

            if hasWon:
                return(sum(list(map(int, unused_numbers))) * int(puzzle_numbers[moves - 1]), moves)
        
        return (0, 1000)

    winning_moves = 1000
    winning_score = 0

    for board in puzzle_boards:
        calculated_board = calculate_board(board)
        if calculated_board[1] < winning_moves:
            winning_moves = calculated_board[1]
            winning_score = calculated_board[0]

    print("[TASK 1]: " + str(winning_score))

    winning_moves = 0
    winning_score = 0

    for board in puzzle_boards:
        calculated_board = calculate_board(board)
        if calculated_board[1] > winning_moves:
            winning_moves = calculated_board[1]
            winning_score = calculated_board[0]

    print("[TASK 2]: " + str(winning_score))

if __name__ == "__main__":
    main()
