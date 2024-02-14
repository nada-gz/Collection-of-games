import random

board = []


def create_board():
    global board
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)

def show_board():
    global board
    for row in board:
        for item in row:
            print(item, end=" ")
        print()

def is_player_win(player):
    win = None

    n = len(board)

    #def _base_player_win(player,cond):
    #    # checking rows
    #    for i in range(n):
    #        win = True
    #        for j in range(n):
    #            a =  exec(f'print({cond})')
    #            print(a)
    #            if a:
    #                win = False
    #                break
    #        if win:
    #            return win
    #print(_base_player_win(player,"board[i][j] != player")) #rows
    # checking rows
    # todo:
    # don't allow position overwriting
    for i in range(n):
        win = True
        for j in range(n):
            if self.board[i][j] != player:
                win = False
                break
        if win:
            return win

    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def is_board_filled():
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def start():
    create_board()
    global board
    player = random.choice(["X", "O"])
    while True:
        print(f"Player {player} turn")

        for row in board:
            for item in row:
                print(item, end=" ")
            print()

        # taking user input
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot: ").split()))
        print()

        board[row - 1][col - 1] = player

        # checking whether current player is won or not
        if is_player_win(player):
            print(f"Player {player} wins the game!")
            break

        # checking whether the game is draw or not
        if is_board_filled():
            print("Match Draw!")
            break

        # swapping the turn
        player = "X" if player=="O" else "O"

        # showing the final view of board
        print()
        show_board()

start()
