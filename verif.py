def verif(board, player):
    if board[0][0]== player and board [0][1]==player and board[0][2]== player or \
        board[1][0] == player and board [1][1] == player and board[1][2]== player or \
        board[2][0] == player and board [2][1] == player and board[2][2]== player or \
        board[0][0] == player and board [1][0] == player and board[2][0]== player or \
        board[0][1] == player and board [1][1] == player and board[2][1]== player or \
        board[0][2] == player and board [1][2] == player and board[2][2]== player or \
        board[0][0] == player and board [1][1] == player and board[2][2]== player or \
        board[0][2] == player and board [1][1] == player and board[2][0]== player:
        print (f"Player {player} Gagne")
        winner = True
        return winner
    if board[0][0] != "1" and board[0][1] != "2" and board[0][2] != "3" and \
    board[1][0] != "4" and board[1][1] != "5" and board[1][2] != "6" and \
    board[2][0] != "7" and board[2][1] != "8" and board[2][2] != "9" :
        print ("match nul !")
        winner = True
        return winner
    else:
        winner = False
    return winner