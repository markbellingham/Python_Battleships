from random import randint
import subprocess as sp

board = []
turn = 1
ships = []
ships_down = 0
game_length = 6



for x in range(5):
    board.append(["O"] * 5)



def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))



while len(ships) < 3:
    ship = []
    ship.append(random_row(board))
    ship.append(random_col(board))
    if ship not in ships:
        ships.append(ship)



def print_board(board):
    global turn
    global game_length
    global message
    tmp = sp.call('clear',shell=True)
    print "Let's play Battleship!"
    print
    for row in board:
        print " ".join(row)
    print
    for i in range(len(ships)):
        print "ship " + str(i) + ":",ships[i]
    print
    try:
        print "Guess is: ", guess
    except NameError:
        print
    print
    try:
        print message
    except NameError:
        print NameError
    if turn < game_length:
        print "Turn:", turn



def make_guess():
    guess = []
    while True:
        try:
            guess_row = int(raw_input("Guess Row: "))
            break
        except ValueError:
            print "That input is not valid"
    while True:
        try:
            guess_col = int(raw_input("Guess Col: "))
            break
        except ValueError:
            print "That input is not valid"
    guess = [guess_row, guess_col]
    return guess



def ship_attack(guess):
    global ships_down
    global game_length
    guess_row = guess[0]
    guess_col = guess[1]
    for ship in ships:
        if guess == ship:
            message = "Congratulations! You sunk battleship", ship
            board[guess_row - 1][guess_col - 1] = "X"
            ships_down += 1
            return message
        else:
            if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                message = "Oops, that's not even in the ocean."
                return message
            elif(board[guess_row - 1][guess_col - 1] == "^"):
                message = "You guessed that one already."
                if turn == game_length:
                    message = "Game Over"
                    return message
            else:
                message = "You missed my battleship!"
                board[guess_row - 1][guess_col - 1] = "^"
                if turn == game_length:
                    message = "Game Over"
                    return message
        if ships_down == len(ships):
            message = "Congratulations! You sunk all my battleships!"
            return message
    return message



for turn in range(1,game_length):
    print_board(board)
    guess = make_guess()
    ship_attack(guess)
    turn += 1


# Extra Credit

# Make multiple battleships you will need to be careful because you need to make sure that you don not place battleships on top of each other on the game board. 
# You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you will 
# need to make sure you don not accidentally place part of a ship off the side of the board.

# Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, statistics and more!