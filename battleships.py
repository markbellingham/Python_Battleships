from random import randint
import subprocess as sp

board = []
message = ""
turn = 1
ships = []
ships_down = 0
game_length = 10

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    global message
    global turn
    global game_length
    tmp = sp.call('clear',shell=True)
    print "Let's play Battleship!"
    print
    for row in board:
        print " ".join(row)
    print 
    print message
    message = ""
    # Print (turn + 1) here unless game is over
    if turn < game_length:
        print "Turn:", turn

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def ship_attack(guess):
    global ships_down
    global message
    global game_length
    for ship in ships:
        if guess == ship:
            print "Congratulations! You sunk battleship", ship
            board[guess_row][guess_col] = "X"
            ships_down += 1
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                message = "Oops, that's not even in the ocean."
                break
            elif(board[guess_row][guess_col] == "^"):
                message = "You guessed that one already."
                if turn == game_length - 1:
                    message = "Game Over"
                break
            else:
                message = "You missed my battleship!"
                board[guess_row][guess_col] = "^"
                #guess_row = ""
                #guess_col = ""
                if turn == game_length - 1:
                    message = "Game Over"
                break
        if ships_down == len(ships):
            break

while len(ships) < 3:
    ship = []
    ship.append(random_row(board))
    ship.append(random_col(board))
    if ship not in ships:
        ships.append(ship)

for turn in range(1,game_length):
    guess = []
    while True:
        try:
            guess_row = int(raw_input("Guess Row: ")) - 1
            break
        except ValueError:
            print "That input is not valid"
    while True:
        try:
            guess_col = int(raw_input("Guess Col: ")) - 1
            break
        except ValueError:
            print "That input is not valid"
    guess.append(guess_row)
    guess.append(guess_col)
    ship_attack(guess)
    
    turn = turn + 1
    print_board(board)


# Extra Credit

# Make multiple battleships you will need to be careful because you need to make sure that you don not place battleships on top of each other on the game board. 
# You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you will 
# need to make sure you don not accidentally place part of a ship off the side of the board.

# Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, statistics and more!