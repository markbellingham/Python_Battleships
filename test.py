from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ships = []
ship = []

while len(ships) < 3:
    #ship = []
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship.append(ship_row)
    ship.append(ship_col)
    if ship not in ships:
        ships.append(ship)

for i in range(len(ships)):
    ship = ships[i]
    for j in ship:
        ship_row = j[0]
        ship_col = j[1]
        print "ship" + i + ":",ship_row, ship_col