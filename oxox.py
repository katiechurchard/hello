board=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]


def draw_board():
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[row]):
            print(board[row][col], end="")
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
            print("winner in horizontal row %i", row)
            return True
    # Check verticals
    for col in range(0, 3):
        if board[0][col] != " " and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            print("winner in vertical col %i", col)
            return True
    # Check diags!
    if ((board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or
        (board[2][0] != " " and board[2][0] == board[1][1] and board[1][1] == board[2][0])):
            print("winner in diagonal")
            return True
    return False


def make_move():
    row = int(input("select row number "))
    col = int(input("select col number "))
    if board[row][col] == " ":
        x = input ("select x or o ")
    return row, col, x


def main():
    # Start of the program
    print(make_move()) 


if __name__ == '__main__':
    main()
