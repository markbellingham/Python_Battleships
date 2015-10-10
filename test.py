from random import randint

# this holds information about how the board is constructed
board = []
count1 = 0
count2 = 0
count3 = 0

# This creates the board
for x in range(5):
    board.append(["O"] * 5)

# Two functions to select a random point on the board
def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ships = []

while len(ships) < 3:
    ### To create a ship of 3 squares ###
    ships = [] # clear the ships list in case of bad result last time the loop executed
    ship = [] # clear for each new ship created
    # Add the first co-ordinate
    ship.append([random_row(board),random_col(board)])
    while len(ship) < 3:
        count1 += 1 # counts how many times the while loop executes to get a valid result
        print "Ship 1 try number " + str(count1)
        # Create the second co-ordinate
        row = random_row(board)
        col = random_col(board)
        # four if statements in 2 parts to check co-ordinates 1, 2 and 3 are next to each other
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
    # When a valid ship has been created, add it to the list of ships
    ships.append(ship)


    ### To create a ship of 2 squares ###
    ship = [] # creating a new ship
    # Add the first co-ordinate
    ship.append([random_row(board),random_col(board)])
    while len(ship) < 2:
        count2 += 1 # counts how many times the loop executes to get a valid result
        print "Ship 2 try number " + str(count2)
        # create a second co-ordinate
        row = random_row(board)
        col = random_col(board)
        # check co-ordinate 2 is next to co-ordinate 1
        if (
            (row == ship[0][0]+1 and col == ship[0][1]) or 
            (row == ship[0][0]-1 and col == ship[0][1]) or 
            (col == ship[0][1]+1 and row == ship[0][0]) or 
            (col == ship[0][1]-1 and row == ship[0][0])
           ):
            ship.append([row,col])
            # make sure that ship number 2 does not overlap ship number 1
            unique = True
            for i in ships:
                for j in ship:
                    if i == j:
                        unique = False
                        break
            if unique == True:
                # When we have a valid ship, add it to the list of ships
                ships.append(ship)
                break


    ### To create a ship of 1 square ###
    count3 += 1 # counts how many times the loop executes to get a valid result
    print "Ship 3 try number " + str(count3)
    ship = [] # creating a new ship
    ship.append(random_row(board))
    ship.append(random_col(board))
    # make sure it is not on top of ships 1 and 2
    unique = True
    for each in ships:
        for part in each:
            if ship == part:
                unique = False
                break
    if unique == True:
        # add it to the list of ships
        ships.append(ship)



print
print ships
print
for i in range(len(ships)):
    print "ship " + str(i + 1) + ":",ships[i]
print