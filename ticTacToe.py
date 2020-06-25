def main():
    while True:
        Play()
        again = input("Do you want to play again? (y / n): ")
        if (again != "y"):
            break


def Play():
    board = [[1], [2], [3],
             [4], [5], [6],
             [7], [8], [9]
             ]
    displayBoard(board)

    player = True
    count = 0
    win = False

    while count != 9:
        ans = int(input("Mark an untaken spot: "))
        while taken(board, ans, player):
            ans = int(input("Mark an untaken spot: "))

        displayBoard(board)
        count += 1

        if (playerWon(board, player)):
            break

        if player:
           player = False
        else:
            player = True

    if count == 9 and not playerWon(board, player):
        print("Its a Draw!")
    elif player:
        print("Player 1 Won!")
    else:
        print("Player 2 Won!")


def taken(board, spot, player):
    if board[spot -1][0] != spot:
        return True
    if player:
        board[spot - 1][0] = 'X'
    else:
        board[spot - 1] = 'O'

    return False 


def displayBoard(board):
    print()
    for i in range(len(board)):
        print("| ", end="")
        print(board[i][0], end=" ")
        if ( (i + 1) % 3 == 0 and (i + 1) != 9):
            print("|")
            print("|___|___|___|")
    print("|")
    print()


def playerWon(board, player):
    letter = ''
    if player:
        letter = 'X'
    else:
        letter = 'O'
    
    if letter == board[0][0] and letter == board[3][0] and letter == board[6][0]:
        return True
    
    if letter == board[0][0] and letter == board[1][0] and letter == board[2][0]:
        return True

    if letter == board[0][0] and letter == board[4][0] and letter == board[8][0]:
        return True

    if letter == board[1][0] and letter == board[4][0] and letter == board[7][0]:
        return True

    if letter == board[2][0] and letter == board[4][0] and letter == board[6][0]:
        return True
    
    if letter == board[2][0] and letter == board[5][0] and letter == board[8][0]:
        return True

    if letter == board[3][0] and letter == board[4][0] and letter == board[5][0]:
        return True

    if letter == board[6][0] and letter == board[7][0] and letter == board[8][0]:
        return True
    
    return False

main()