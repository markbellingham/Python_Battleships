from random import randint
import subprocess as sp

board = []
message = ""
turn = 1

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    global message
    global turn
    tmp = sp.call('clear',shell=True)
    print "Let's play Battleship!"
    print
    for row in board:
        print " ".join(row)
    print 
    print message
    message = ""
    # Print (turn + 1) here unless game is over
    if turn < 6:
        print "Turn:", turn

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)
while True:
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    if ship2_row != ship1_row or ship2_col != ship1_col:
        break

print "ship 1 is: ", ship1_row, ship1_col
print "ship 2 is: ", ship2_row, ship2_col

for turn in range(1,6):
    while True:
        try:
            guess_row = int(raw_input("Guess Row: ")) - 1
            break
        except ValueError:
            print "Invalid value"
    while True:
        try:
            guess_col = int(raw_input("Guess Col: ")) - 1
            break
        except ValueError:
            print "Invalid value"
    
    if guess_row == ship1_row and guess_col == ship1_col:
        print "Congratulations! You sunk my battleship number 1!"
        board[guess_row][guess_col] = "X"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            message = "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "^"):
            message = "You guessed that one already."
            if turn == 5:
                message = "Game Over"
        else:
            message = "You missed my battleship!"
            board[guess_row][guess_col] = "^"
            if turn == 5:
                message = "Game Over"
        turn = turn + 1
        print_board(board)


# Extra Credit

# Make multiple battleships you will need to be careful because you need to make sure that you don not place battleships on top of each other on the game board. 
# You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you will 
# need to make sure you don not accidentally place part of a ship off the side of the board.

# Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, statistics and more!