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


def user_move(board,player):
    move = input("Entrez votre mouvement (1-9): ")

    if move == "1":
        board[0][0] = player
    elif move == "2":
        board[0][1] = player
    elif move == "3":
        board[0][2] = player
    elif move == "4":
        board[1][0] = player
    elif move == "5":
        board[1][1] = player
    elif move == "6":
        board[1][2] = player
    elif move == "7":
        board[2][0] = player
    elif move == "8":
        board[2][1] = player
    elif move == "9":
        board[2][2] = player
    else: 
        print(f"Mouvement {move} invalide")



def check_win (board, player):
    #String validation
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            print(f"Joueur {player}, vous avez gagné!")
            return True

    #Column validation
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            print(f"Joueur {player}, vous avez gagné!")
            return True
        
    #Diagonales verification
   # if board[0][0] == board[1][1] == board[2][2] != "-":
    #    print(f"Joueur {player}, vous avez gagné!")
     #   return True
        
    if board[0][2] == board[1][1] == board[2][0] != "-":
        print(f"Joueur {player}, vous avez gagné!")
        return True
    
    return None

# Check if it is a draw
def check_draw(board):
    for row in board:
        if any(cell not in ["X", "O"] for cell in row):  # If the box is not occupied
            return False
    print("C'est un tirage au sort. Essayez à nouveau")
    return True


# Fonction principale pour orchestrer le jeu
def play_game():
    # Création du plateau
    board = create_board()
    print_board(board)

    # Initialisation du joueur actif
    player = "X"

    while True:
        print(f"C'est au tour du joueur {player}.")
        user_move(board, player)  # Demander le mouvement
        print_board(board)  # Afficher le plateau mis à jour

        # Vérifier si le joueur actuel a gagné
        if check_win(board, player):
            print(f"Félicitations, joueur {player}! Vous avez gagné!")
            break

        # Vérifier si la partie est nulle
        if check_draw(board):
            print("C'est un match nul!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

# Appel de la fonction principale pour démarrer le jeu
play_game()




