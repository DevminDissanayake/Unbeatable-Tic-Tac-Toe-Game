import random

boardWidth = 3;
boardLength = 3;

def new_board():
    newBoard = [[0 for x in range (boardWidth)]for y in range(boardLength)]
    for x in range(0,3):
        for y in range(0,3):
            newBoard[x][y] = None


    return newBoard

def render(newBoard):
    for z in range(0,3):
        if(z==0):
            print("   ")
    print(z + "  ")
print("\n")
for a in range(0,7):
        if(a == 0):
            print("  ")
print("*")
for i in range(0,3):
    print(i + " " + "|" + " ");

    for j in range(0,3):
                if(newBoard[j][i] == None):
                    newBoard[j][i] = "_"
                else:
                    print(newBoard[j][i] + " ")
                if(j==2):
                    print("|" + "\n" + "\n")
    for b in range(0,7):
        if(b==0):
            print("  ")
    print("*")


board = new_board()
board[0][1] = 'X'
board[1][1] = '0'
print(render(board))