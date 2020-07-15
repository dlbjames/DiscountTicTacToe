# Creates the board for us to play on
# and updates the board as the players take
# their turns.
def play():
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    displayBoard(board)
    player = 'X'
    count = 0

    while count != 9:
        # AI's Move
        if count % 2:
            (maxMove, x, y) = getMax(board, player)
            print("AI's Move: {}, {}".format(x, y))
            print()
            
            # Calculates the position on the board (1, 2, 3, 4, 5, ..., 9)
            taken(board, (3 * x) + y + 1, player)

        #Player's Move
        else:
            (minMove, minX, minY) = getMin(board, player)
            print("Recommended Move: {}".format((3 * minX) + minY + 1))
            print()
            ans = int(input("Mark an untaken spot: "))
            while taken(board, ans, player):
                ans = int(input("Mark an untaken spot: "))

        displayBoard(board)
        count += 1

        if playerWon(board, player) == player:
            break
        # Change the player's turns
        if player == 'X':
           player = 'O'
        else:
            player = 'X'

    if count == 9 and playerWon(board, player) != player:
        print("Its a Draw!")
    elif 'X' == playerWon(board, player):
        print("You beat the AI!")
    else:
        print("The AI Won!")

# Determines if a spot on the board
# is already taken. 
def taken(board, spot, player):
    if board[(spot - 1) // 3][spot % 3 - 1] != spot:
        return True
    if player == 'X':
        board[(spot - 1) // 3][spot % 3 - 1] = 'X'
    else:
        board[(spot - 1) // 3][spot % 3 - 1] = 'O'
    return False 

# Displays the board to the console.
def displayBoard(board):
    print()
    for i in range(len(board)):
        print("| ", end="")
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
            print("|", end=" ")

        print()
        if i != 2:
            print("|___|___|___|")
        else:
            print("|   |   |   |")
    print()

# Determines if a player has won the game.
def playerWon(board, player):
    # Horizontal Win
    for i in range(0, 3):
        if [player, player, player] == board[i]:
            return player

    # Vertical Win
    for i in range(0, 3):
        if board[0][i] == player and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return player

    # Top Left Diagonal Win
    if board[0][0] == player and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return player

    # Top Right Diagonal Win
    if board[0][2] == player and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return player

    # Check if there are still empty spots
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                return None
    
    return '.'

# Gets the computer's move that causes
# the 'greatest' chance of winning.
def getMax(board, player):
    maxMove = -2
    px = None
    py = None
    
    result = playerWon(board, player)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    # For each possible move left
    # Check if that move is a 'good move'.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                temp = board[i][j]
                board[i][j] = 'O'
                (minMove, min_i, min_j) = getMin(board, player)
                if minMove > maxMove:
                    maxMove = minMove
                    px = i
                    py = j
                board[i][j] = temp
    return (maxMove, px, py) 

# Gets the computer's move that 
# causes the 'least' chance of a loss.
def getMin(board, player):
    minMove = 2
    qx = None
    qy = None
    
    # Result is the player variable
    result = playerWon(board, player)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    # For each possible move left
    # Check if that move is a 'good move'.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                temp = board[i][j]
                board[i][j] = 'X'
                (maxMove, max_i, max_j) = getMax(board, player)

                if maxMove < minMove:
                    minMove = maxMove
                    qx = i
                    qy = j
                board[i][j] = temp
    return (minMove, qx, qy) 

# The main game loop that allows us
# to play the game asking for input 
# when the game is finished.
def main():
    while True:
        play()
        again = input("Do you want to play again? (y / n): ")
        if (again != "y"):
            break

if __name__ == "__main__":
    main()