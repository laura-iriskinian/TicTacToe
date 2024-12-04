def create_board():
    board = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
    ]
    return board

def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


def user_move(board,player,boelan):
    move = input("Entrez votre mouvement (1-9): ")
    if move == "1" and board[0][0] == "1":
        board[0][0] = player
        boelan = True
        return boelan
    elif move == "2" and board[0][1] == "2":
        board[0][1] = player
        boelan = True
        return boelan
    elif move == "3" and board[0][2] == "3":
        board[0][2] = player
        boelan = True
        return boelan
    elif move == "4" and board[1][0] == "4":
        board[1][0] = player
        boelan = True
        return boelan
    elif move == "5" and board[1][1] == "5":
        board[1][1] = player
        boelan = True
        return boelan
    elif move == "6" and board[1][2] == "6":
        board[1][2] = player
        boelan = True
        return boelan
    elif move == "7" and board[2][0] == "7":
        board[2][0] = player
        boelan = True
        return boelan
    elif move == "8" and board[2][1] == "8":
        board[2][1] = player
        boelan = True
        return boelan
    elif move == "9" and board[2][2] == "9":
        board[2][2] = player
        boelan = True
        return boelan
    else: 
        print(f"Mouvement {move} invalide")
        boelan = False
        return boelan


board = create_board()
print_board(board)

def verif(board, player):
    if board[0][0]== player and board [0][1]==player and board[0][2]== player: #ligne 1
        print (f"Player {player} Gagne")
        winner = True
        return winner
    elif board[1][0] == player and board [1][1] == player and board[1][2]== player: #ligne 2
        print (f"Player {player} Gagne")
        winner = True
    elif board[2][0] == player and board [2][1] == player and board[2][2]== player: #ligne 3
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][0] == player and board [1][0] == player and board[2][0]== player: #colonne 1
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][1] == player and board [1][1] == player and board[2][1]== player: #colonne 2
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][2] == player and board [1][2] == player and board[2][2]== player: #colonne 3
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][0] == player and board [1][1] == player and board[2][2]== player: #diagonale de gauche à droite
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][2] == player and board [1][1] == player and board[2][0]== player: #diagonale de droite à gauche
        print (f"Player {player} Gagne")
        winner = True
    elif board[0][0] != "1" and board[0][1] != "2" and board[0][2] != "3" and \
    board[1][0] != "4" and board[1][1] != "5" and board[1][2] != "6" and \
    board[2][0] != "7" and board[2][1] != "8" and board[2][2] != "9" :
        print (f"match nul !")
        winner = "Nul"
    else:
        winner = False
        return winner


# exemple pour pouvoir jouer --> boucle à créer
winner = False
player = "X"
boelan=any



while winner == False:

    print (f"joueur: {player}") 

    boelan = user_move(board, player, boelan)

    print_board (board)

    winner=verif(board, player)

    if player == "X" and boelan == True:
        player = "O"
    elif player == "O" and boelan == True:
        player = "X"

    if winner == True:
        print("Voulez vous rejouer ?")
        reset = input("Rentrez yes ou no : ")
        if reset == "Yes":
            board = create_board()
            print_board(board)
            winner = False
            player = "X"  
        else:
            print("A bientôt !!") 
            winner = True 
        