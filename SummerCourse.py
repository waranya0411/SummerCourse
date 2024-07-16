import random

ROWS = 6
COLS = 7

def create_board():
    return [[0] * COLS for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print('-' * COLS * 2)

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def is_draw(board):
    return all(board[0][col] != 0 for col in range(COLS))

def get_valid_locations(board):
    return [col for col in range(COLS) if is_valid_location(board, col)]

def computer_move(board):
    valid_locations = get_valid_locations(board)
    return random.choice(valid_locations)

def main():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("PLAYER 1 WINS!")
                    game_over = True
        else:
            col = computer_move(board)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("COMPUTER WINS!")
                    game_over = True

        print_board(board)

        if is_draw(board):
            print("It's a draw!")
            game_over = True

        turn += 1
        turn = turn % 2

if __name__ == "__main__":
    main()
