'''
Tic-tac-toe by Ran Libeskind-Hadas
Modified by Brian Borowski, 10/28/2014
Updated to Python 3 on 01/23/2016
Minor modifications on 10/31/2018
'''
debug = False

def main():
    '''This is the main function for the tic-tac-toe game'''
    welcome()
    while True:
        if debug: print('About to enter playGame()')
        playGame()
        response = input('Would you like to play again? (y or n): ').strip()
        if not response in ['y', 'Y', 'yes', 'Yes', 'Yup', 'si', 'oui',
                            'youbetcha']:
            print('Bye!')
            return

def welcome():
    '''Prints the welcome message for the game.
       We might also print the rules for the game and any other
       information that the user might need to know.'''
    print('Welcome to tic-tac-toe!')

def playGame():
    '''Play one game of tic-tac-toe'''
    if debug:  print('Entering the playGame() function')
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 1
    print('The board looks like this:')
    printBoard(board)
    while not gameOver(board):
        getMove(board, player)
        if player == 1: player = 2
        else: player = 1
        print('The board looks like this:')
        printBoard(board)

def gameOver(board):
    '''Returns False if the game is NOT over.  Otherwise, prints a message
       indicating which player has won and then returns True indicating that the
       game is over.'''
    if debug:  print('Entering the gameOver function')
    winner = getWinner(board)
    if winner == '1':
        print('Player 1 wins!')
        return True
    if winner == '2':
        print('Player 2 wins!')
        return True
    if boardFull(board):
        print('Tie.')
        return True
    return False

def getMove(board, player):
    '''Takes the board and the current player (1 or 2) as input.
        Asks the player for her/his move.  If it's a legitimate move,
        the change is made to the board.  Otherwise, the player
        is queried again until a valid move is provided.'''
    print('Player ' + str(player) + '\'s turn')
    while True:
        try:
            row = int(input('Enter the row: ').strip())
            column = int(input('Enter the column: ').strip())
            if row < 0 or row > 2 or column < 0 or column > 2:
                print('That\'s not a valid location on the board! Try again.')
            elif board[row][column] != ' ':
                print('That cell is already taken! Try again.')
            else:
                board[row][column] = str(player)
                break
        except:
            print('That\'s not a valid input! Try again.')

def printBoard(board):
    if debug:  print('Entering the printBoard() function')
    for row in range(0, 3):
        print(' ', end='')
        for column in range(0, 3):
            print(board[row][column], end=' ')
            if column < 2: print('|', end=' ')
        print()  # CAUSES A LINEBREAK!
        if row < 2: print('-' * 11)

def boardFull(board):
    if debug:  print('Entering the boardFull() function')
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

def getWinner(board):
    if debug:  print('Entering the getWinner() function')
    # Check rows
    for row in range(3):
        val = board[row][0]
        if val != ' ':
            col = 1
            while col < 3:
                if board[row][col] != val:
                    break
                col += 1
            if col == 3:
                return val
    # Check columns
    for col in range(3):
        val = board[0][col]
        if val != ' ':
            row = 1
            while row < 3:
                if board[row][col] != val:
                    break
                row += 1
            if row == 3:
                return val
    # Check major diagonal
    val = board[0][0]
    if val != ' ':
        index = 1
        while index < 3:
            if board[index][index] != val:
                break;
            index += 1
        if index == 3:
            return val
    # Check minor diagonal
    val = board[0][2]
    if val != ' ':
        index = 1
        while index < 3:
            if board[index][3 - index - 1] != val:
                break;
            index += 1
        if index == 3:
            return val
    return ' '

if __name__ == '__main__':
    main()
