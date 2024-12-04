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

def verif(board):
    if board[0][0] == "X":
        print ("Gagner")
        winner = True
        return winner
    else:
        winner = False
        return winner
    

# exemple pour pouvoir jouer --> boucle à créer
winner = False
player = "X"
boelan=any
while winner == False:
    winner = verif(board)
    if winner == False:
        if player == "X":
            print("Joueur X:")
            boelan = user_move(board, player, boelan)  # Rappeler la fonction correctement
            print_board(board)
            if boelan == True:
                player = "O"
            else:
                print(f"Player {player}, veuillez rejouer.") # Pas besoin de rappeler la fonction print_board dans else
        else:
            print("Joueur O:")
            boelan = user_move(board, player, boelan)  # Rappeler la fonction correctement 
            print_board(board)
            if boelan == True:
                player = "X"
            else:
                print(f"Player {player}, veuillez rejouer.") # Pas besoin de rappeler la fonction print_board dans else
