# Elick Coval
# 00845725
# Elick_Coval@student.uml.edu
# 2/17/2020
# COMP 4600
# HW 4


import random
import numpy as np

rand = random.randint(1, 100)
board = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
numberLookUp = {'1': '00', '2': '01', '3': '02', '4': '10', '5': '11', '6': '12', '7': '20', '8': '21', '9': '22'}
rows = board.shape[0]
cols = board.shape[1]
p1Token = "A"
p2Token = "B"


# class for keeping track of the game status
class gameTracker:

    boardPieces = 0

    def __init__(self, gameOver, pATurn, player, boardPieces):
        self.gameOver = gameOver
        self.pATurn = pATurn
        self.player = player
        self.boardPieces = boardPieces

    def gameOver(self):
        return self.gameOver

    def winner(self):
        return self.winner

    def pATurn(self):
        return self.pATurn

    def player(self):
        return self.player

    def boardPieces(self):
        return self.boardPieces

    def addToBoard(self, boardPieces):
        self.boardPieces += boardPieces


# locate which slot the player selected and look for a win
def boardPick(pick, token, game):
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == str(pick):
                print("Pick is " + str(pick))
                board[x][y] = token
                game.addToBoard(1)
    if lookForWin(token, game):
        game.gameOver = True


# if a win is found, reflect that
def lookForWin(token, game):
    win = False
    if lookForColWin(token) or lookForRowWin(token) or lookForDiagWin(token):
        game.winner = token
        win = True
    return win


# check columns for win
def lookForColWin(token):
    win = False
    for x in range(rows):
        tally = 0
        for y in range(cols):
            if board[y][x] == token:
                tally += 1
                if tally == 3:
                    return True
    return win

# check rows for win, opposite method for columns
def lookForRowWin(token):
    win = False
    for x in range(rows):
        tally = 0
        for y in range(cols):
            if board[x][y] == token:
                tally += 1
                if tally == 3:
                    return True
    return win


# check diag for win, this one was tricky, had to hack it a little bit
def lookForDiagWin(token):
    win = False
    tally = 0
    for x in range(rows):
        if board[x][x] == token:
            tally += 1
            if tally == 3:
                return True

    tally = 0
    y = 2
    for x in range(rows):
        if board[x][y] == token:
            tally += 1
            if tally == 3:
                return True
        y -= 1
    return win


# use dictionary for precise location of each number on the board and find it's index easily
def takenSlot(pick):
    index = numberLookUp[str(pick)]
    x = int(index[0])
    y = int(index[1])
    if board[x][y] == "A" or board[x][y] == "B":
        print("A player already has a piece there!\n")
        print("Please pick a different slot\n ")
        return True
    return False


def resetBoard():
    num = '1'
    for x in range(rows):
        for y in range(cols):
            board[x][y] = num
            num = int(num) + 1
            num = str(num)


def newGameAsk():
    quit = input("New Game? (y/n)")
    if quit == 'y' or quit == 'Y':
        resetBoard()
        return False
    else:
        return True

# Where the main action happens
def playGame():

    # gameTracker keeps track of if the game is over, player A's turn , current player token, number of tokens on the
    # board
    game = gameTracker(False, True, "A", 0)

    while True:

        print(board)

        playerPick = int(input("Player " + str(game.player) + "'s Turn, type 0 to quit \n"))

        # Validate before playing
        if playerPick < 0 or playerPick > 9 or playerPick == '':
            print("INVALID: Please pick a value on the board")

        # quit before playing a turn
        elif playerPick == 0:
            if newGameAsk():
                exit(1)
            else:
                game = gameTracker(False, True, "A", 0)

        # player A
        elif game.pATurn:
            if not takenSlot(playerPick):
                boardPick(playerPick, p1Token, game)
                game.pATurn = False
                game.player = p2Token
        # player B
        else:
            if not takenSlot(playerPick):
                boardPick(playerPick, p2Token, game)
                game.pATurn = True
                game.player = p1Token

        # somebody won
        if game.gameOver:
            print("Congratulations " + str(game.winner) + " wins!!!")
            print(board)
            if newGameAsk():
                exit(1)
            else:
                game = gameTracker(False, True, "A", 0)

        # board is full
        if game.boardPieces == 9:
            print(board)
            print("It's a Draw!! No spaces left!\n")
            print(board)
            if newGameAsk():
                exit(1)
            else:
                game = gameTracker(False, True, "A", 0)


playGame()
