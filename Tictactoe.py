turn = 0
winstate = False
winline_length = 3
players = 2 #int(input("Number of players: "))
pieces = ["X", "O"]
borders = False #input("Draw borders? ")


#Create a board array of size (x, y)
def make_board(x, y):
    board = [["   " for a in range(x)] for b in range(y)]
    return board

#Draw board array in console as ASCII drawing with no optional borders
def draw_board(board):
    global borders
    height = len(board)
    width = len(board[0])
    horizontal_border = "" if borders == False else "-"
    vertical_border = "" if borders == False else "|"
    for i in range(width):
        if i < width - 1 or i == width - 1 and borders == True:
            horizontal_border += "----"
        else:
            horizontal_border += "---"
    for i in range(height):
        for j in range(width):
            if j < width - 1 or j == width - 1 and borders == True:
                vertical_border += board[i][j] + "|"
            else:
                vertical_border += board[i][j]
        if i == 0 and borders == True:
            print(horizontal_border)
        print(vertical_border)
        vertical_border = "" if borders == False else "|"
        if i < height - 1 or i == height - 1 and borders == True:
            print(horizontal_border)

#Return index of current player's turn with input of total number of players
def player_turn(x):
    global turn
    return turn % x

#Incriment the turn counter
def turn_inc():
    global turn
    turn += 1
    return

gameboard = make_board(3, 3)

def check_win(board):
    global winline_length
    global winstate
    wintest = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "   ":
                if j <= len(board[0]) - winline_length:
                    for k in range(winline_length):
                        wintest.append(board[i][j + k])
                        for n in wintest:
                            if 
                    if board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        winstate = True
                        return
                    if i >= winline_length - 1:
                        if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2]:
                            winstate = True
                            return
                    if i <= len(board) - winline_length:
                        if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]:
                            winstate = True
                            return
                if i <= len(board) - winline_length:
                    if board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        winstate = True
                        return

def move(x, y):
    global turn
    global winline_length
    global players
    global pieces
    global gameboard
    player_piece = pieces[player_turn(players)]
    if gameboard[y][x] == "   ":
        gameboard[y][x] = " " + player_piece + " "
        check_win(gameboard)
        if winstate == True:
            print("")
            draw_board(gameboard)
            print("")
            print("Player " + str(player_turn(players) + 1) + " wins..")
            return
        turn_inc()
    else:
        print("Not a legal move..")
    print("")
    draw_board(gameboard)

        
draw_board(gameboard)
while winstate == False:
    x = int(input("Move column: "))
    y = int(input("Move row: "))
    move(x, y)