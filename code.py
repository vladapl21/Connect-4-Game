board = [[' ' for _ in range(7)] for _ in range(6)]


def print_board():
    for row in board:
        print(' | '.join(row))
    print('-' * 13)


def make_move(player, column):
    for i in range(6):
        if board[5 - i][column] == ' ':
            board[5 - i][column] = player
            return
    print("Invalid move")


def check_winner():
    # Check horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] != ' ' and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                return board[i][j]
    # Check vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] != ' ' and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                return board[i][j]
    return None


def main():
    player = 'X'
    while True:
        print_board()
        column = int(input("Player {} make your move (0-6): ".format(player)))
        make_move(player, column)
        winner = check_winner()
        if winner:
            print_board()
            print("Player {} wins!".format(winner))
            break
        player = 'O' if player == 'X' else 'X'


main()
