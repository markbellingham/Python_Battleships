from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ships = []

while len(ships) < 3:
    ship = []
    ship.append(random_row(board))
    ship.append(random_col(board))
    if ship not in ships:
        ships.append(ship)

for i in range(len(ships)):
    print "ship " + str(i) + ":",ships[i]