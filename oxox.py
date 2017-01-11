board=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]


player = 1


def draw_board():
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            print(board[row][col], end = " ")
            if not col == len(board[row])-1:
                print("|", end="")
            col = col + 1
        if not row == len(board)-1:
            print("\n-----")
        row = row +  1


def check_win():
    # Check horizontal
    for row in range(0, 3):
        if board[row][0] != " " and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            print("winner in horizontal row %i" % row)
            return True
    # Check verticals
    for col in range(0, 3):
        if board[0][col] != " " and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            print("winner in vertical col %i" % col)
            return True
    # Check diags!
    if ((board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or
        (board[2][0] != " " and board[2][0] == board[1][1] and board[1][1] == board[0][2])):
            print("winner in diagonal")
            return True
    # Check Not Full Board
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                return False
    # Board is Full
    print("Board is full, Game Over")
    return True


def make_move():
    global player
    print("\nmove for player %i" % player)
    row = int(input("select row number "))
    col = int(input("select col number "))
    if board[row][col] == " ":
        if player == 1:
            x = "X"
            player = 2
        else:
            x = "O"
            player = 1
    else:
        return make_move()
    return row, col, x


def main():
    # Start of the program
    draw_board()
    while not check_win():
        try:
            row, col, x = make_move()
            if board[row][col] == " ":
                board[row][col] = x
            else:
                print("cell not empty")
        except ValueError:
            print("you must enter a number")
        except IndexError:
            print("enter a number between 0 - 2")
        except KeyboardInterrupt:
            print("board must be filled before exiting")
        draw_board()


if __name__ == '__main__':
    main()
