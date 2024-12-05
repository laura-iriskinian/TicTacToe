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
    def can_win(b, p):
        # Vérifie si un coup donne la victoire
        for i in range(3):
            for j in range(3):
                if b[i][j] not in ("X", "O"):
                    temp = b[i][j]
                    b[i][j] = p
                    if verif(b, p):
                        b[i][j] = temp
                        return i, j
                    b[i][j] = temp
        return None

    # 1. Vérifier si l'IA peut gagner
    win_move = can_win(board, signe)
    if win_move:
        board[win_move[0]][win_move[1]] = signe
        return True

    # 2. Bloquer si l'adversaire peut gagner
    opponent = "X" if signe == "O" else "O"
    block_move = can_win(board, opponent)
    if block_move:
        board[block_move[0]][block_move[1]] = signe
        return True

    # 3. Sinon jouer sur une case libre
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ("X", "O"):
                board[i][j] = signe
                return True
    return False

def verif(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player or \
       board[1][0] == player and board[1][1] == player and board[1][2] == player or \
       board[2][0] == player and board[2][1] == player and board[2][2] == player or \
       board[0][0] == player and board[1][0] == player and board[2][0] == player or \
       board[0][1] == player and board[1][1] == player and board[2][1] == player or \
       board[0][2] == player and board[1][2] == player and board[2][2] == player or \
       board[0][0] == player and board[1][1] == player and board[2][2] == player or \
       board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"Player {player} gagne !")
        return True

    # Vérifier s'il y a match nul
    if all(board[i][j] in ("X", "O") for i in range(3) for j in range(3)):
        print("Match nul !")
        return True
    
    return False

# Initialisation du jeu
board = create_board()
print_board(board)

winner = False
player = "X"

while not winner:
    print(f"Joueur: {player}")
    if player == "X":
        valid_move = user_move(board, player)
    else:
        valid_move = IA(board, player)

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
            print("A bientôt !!")
            winner = True
