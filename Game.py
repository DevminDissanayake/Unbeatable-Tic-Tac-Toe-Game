

boardWidth = 3
boardLength = 3


def new_board():
    newBoard = []
    for x in range(0, boardWidth):
        column = []
        for y in range(0, boardLength):
            column.append(None)
        newBoard.append(column)

    return newBoard


def render(newBoard):
    rows = []
    for y in range(0, boardLength):
        row = []
        for x in range(0, boardWidth):
            row.append(newBoard[x][y])
        rows.append(row)

    row_num = 0
    print('  0 1 2 ')
    print(' *******')
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += '_'
            else:
                output_row += sq
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print(' *******')


def get_move():
    x = int(input("What is your move's X coordinate?:"))
    y = int(input("What is your move's Y coordinate?:"))
    getCoords = [None, None]
    getCoords[0] = x
    getCoords[1] = y
    return getCoords


def make_move(player, board, move_co_ords):
    if board[move_co_ords[0]][move_co_ords[1]] is not None:
        raise Exception("Illegal move!")

    board[move_co_ords[0]][move_co_ords[1]] = player


def get_coordinates():
    columns = []
    for x in range(0, boardWidth):
        column = []
        for y in range(0, boardLength):
            column.append((x, y))
        columns.append(column)
    rows = []
    for y in range(0, boardLength):
        row = []
        for x in range(0, boardWidth):
            row.append((x, y))
        rows.append(row)
    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return columns + rows + diagonals


def get_winner(newBoard):
    allCoordinates = get_coordinates()
    for line in allCoordinates:
        line_values = [newBoard[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]
    return None


def is_it_a_draw(newBoard):
    for column in newBoard:
        for block in column:
            if block is None:
                return False
    return True


def play():
    newBoard = new_board()
    Player1turn = True
    while True:
        while Player1turn is True:
            getCoords = get_move()
            Player = 'X'
            make_move(Player, newBoard, getCoords)
            render(newBoard)
            Player1turn = False
        winner = get_winner(newBoard)
        if winner is not None:
            render(newBoard)
            print("%s has won!" % winner)
            break
        if is_it_a_draw(newBoard) == True:
            render(newBoard)
            print("It's a draw")
            break
        while Player1turn is False:
            getCoords = get_move()
            Player = 'O'
            make_move(Player, newBoard, getCoords)
            render(newBoard)
            Player1turn = True
        winner = get_winner(newBoard)
        if winner is not None:
            render(newBoard)
            print("%s has won!" % winner)
            break
        if is_it_a_draw(newBoard) == True:
            render(newBoard)
            print("It's a draw")
            break


play()
