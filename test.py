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
    valid_move = False
    if move == "1" and board[0][0] == "1":
        board[0][0] = player
        valid_move = True
    elif move == "2" and board[0][1] == "2":
        board[0][1] = player
        valid_move = True
    elif move == "3" and board[0][2] == "3":
        board[0][2] = player
        valid_move = True
    elif move == "4" and board[1][0] == "4":
        board[1][0] = player
        valid_move = True
    elif move == "5" and board[1][1] == "5":
        board[1][1] = player
        valid_move = True
    elif move == "6" and board[1][2] == "6":
        board[1][2] = player
        valid_move = True
    elif move == "7" and board[2][0] == "7":
        board[2][0] = player
        valid_move = True
    elif move == "8" and board[2][1] == "8":
        board[2][1] = player
        valid_move = True
    elif move == "9" and board[2][2] == "9":
        board[2][2] = player
        valid_move = True
    else:
        print(f"Mouvement {move} invalide")
    
    return valid_move

def IA(board, signe):
    signe="O"
    for i in range(3):
        for j in range(3):
            if board[i][j] in "123456789":
                board[i][j] = signe
                return True
    return False

def verif(board, player):
    for i in range(3):  # Vérifie les lignes et les colonnes
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            print(f"Player {player} gagne")
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        print(f"Player {player} gagne")
        return True
    if all(board[i][j] not in "123456789" for i in range(3) for j in range(3)):
        print("Match nul!")
        return True
    return False

board = create_board()
print_board(board)

winner = False
player = "X"

while not winner:
    print(f"Joueur: {player}")
    if player == "X":
        valid_move = user_move(board, player) #si le joueur est X, la fonction user_move s'applque
    else:
        valid_move = IA(board, player) #sinon c'est la fonction auto_move qui s'applique
    
    if valid_move:
        print_board(board)
        winner = verif(board, player)
        player = "O" if player == "X" else "X"

    if winner:
        replay = input("Voulez-vous rejouer ? (oui/non): ")
        if replay.lower() == "oui":
            board = create_board()
            print_board(board)
            winner = False
            player = "X"
        else:
            print("A bientôt !")
