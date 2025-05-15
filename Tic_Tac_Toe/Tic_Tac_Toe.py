from random import randrange

def display_board(board):
    line = "+-------+-------+-------+"
    for row in board:
        print(line)
        print("|       " * 3 + "|")
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print("|       " * 3 + "|")
    print(line)

def enter_move(board):
    valid = False
    while not valid:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                raise ValueError
            row, col = divmod(move - 1, 3)
            if board[row][col] in ['X', 'O']:
                print("Field is already occupied!")
                continue
            board[row][col] = 'O'
            valid = True
        except ValueError:
            print("Invalid move. Please enter a number from 1 to 9.")

def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free.append((i, j))
    return free

def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or \
           all(board[j][i] == sign for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or \
       all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'

def play_game():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    board[1][1] = 'X'  # First move by computer in the center
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
