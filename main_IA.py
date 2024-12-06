def create_board():
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
    return board

def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def user_move(board, player):
    move = input("Entrez votre mouvement (1-9): ")
    boelan = False
    if move == "1" and board[0][0] == "1":
        board[0][0] = player
        boelan = True
    elif move == "2" and board[0][1] == "2":
        board[0][1] = player
        boelan = True
    elif move == "3" and board[0][2] == "3":
        board[0][2] = player
        boelan = True
    elif move == "4" and board[1][0] == "4":
        board[1][0] = player
        boelan = True
    elif move == "5" and board[1][1] == "5":
        board[1][1] = player
        boelan = True
    elif move == "6" and board[1][2] == "6":
        board[1][2] = player
        boelan = True
    elif move == "7" and board[2][0] == "7":
        board[2][0] = player
        boelan = True
    elif move == "8" and board[2][1] == "8":
        board[2][1] = player
        boelan = True
    elif move == "9" and board[2][2] == "9":
        board[2][2] = player
        boelan = True
    else:
        print(f"Mouvement {move} invalide")
    
    return boelan

def IA(board, player):
    player="O"
    for i in range(3):
        for j in range(3):
            if board[i][j] in "123456789":
                board[i][j] = player
                return True
    return False

board = create_board()
print_board(board)

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


# exemple pour pouvoir jouer --> boucle à créer
winner = False
player = "X"

while not winner:
    print(f"Joueur: {player}")
    if player == "X":
        boelan = user_move(board, player) #si le joueur est X, la fonction user_move s'applque
    else:
        boelan = IA(board, player) #sinon c'est la fonction auto_move qui s'applique
    
    if boelan == True:
        print_board(board)
        winner = verif(board, player)
        if player == "X":
            player = "O"
        else:
            player = "X"

    if winner == True:
        print("Voulez vous rejouer ?")
        reset = input("Rentrez oui ou non : ")
        if reset == "oui":
            board = create_board()
            print_board(board)
            winner = False
            player = "X"  
        else:
            print("A bientôt !!") 
            winner = True
        