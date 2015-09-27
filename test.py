from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ships = []

while len(ships) < 3:
    # To create a ship of 3 squares
    ship = []
    ship.append([random_row(board),random_col(board)])
    while len(ship) < 3:
        row = random_row(board)
        col = random_col(board)
        if row == ship[0][0]+1 and col == ship[0][1]:
            ship.append([row,col])
            if row+1 < 6:
                ship.append([row+1,col])
            else:
                ship.append([ship[0][0]-1,col])
        elif row == ship[0][0]-1 and col == ship[0][1]:
            ship.append([row,col])
            if row-1 > 0:
                ship.append([row-1,col])
            else:
                ship.append([row+2,col])
        elif col == ship[0][1]+1 and row == ship[0][0]:
            ship.append([row,col])
            if col+1 < 6:
                ship.append([row,col+1])
            else:
                ship.append([row,ship[0][1]-1])
        elif col == ship[0][1]-1 and row == ship[0][0]:
            ship.append([row,col])
            if col-1 > 0:
                ship.append([row,col-1])
            else:
                ship.append([row,col+2])
    ships.append(ship)
    # To create a ship of 2 squares
    ship = []
    ship.append([random_row(board),random_col(board)])
    while len(ship) < 2:
        row = random_row(board)
        col = random_col(board)
        if (
            (row == ship[0][0]+1 and col == ship[0][1]) or 
            (row == ship[0][0]-1 and col == ship[0][1]) or 
            (col == ship[0][1]+1 and row == ship[0][0]) or 
            (col == ship[0][1]-1 and row == ship[0][0])
           ):
            ship.append([row,col])
    unique = False
    for part in ship:
        if part not in ships:
            unique = True
    if unique == True:
        ships.append(ship)
    # To create a ship of 1 square
    ship = []
    ship.append(random_row(board))
    ship.append(random_col(board))
    if ship not in ships:
        ships.append(ship)



print
print ships
print
for i in range(len(ships)):
    print "ship " + str(i + 1) + ":",ships[i]
print