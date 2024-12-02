# Fonction pour afficher la grille du jeu
def afficher_grille(board):
    for row in board:
        print(" | ".join(map(str, row)))  # Joint les éléments de la ligne avec " | "
        print("-" * 9)  # Affiche une ligne de séparation

# Fonction pour mettre à jour la grille avec le coup du joueur
def update_board(board, position, player): 
    row = (position - 1) // 3  # La division par 3 pour trouver la ligne
    col = (position - 1) % 3   # Le reste (modulo) pour trouver la colonne
    board[row][col] = player  # Met à jour la case avec le symbole du joueur

# Fonction pour demander à un joueur de choisir une case entre 1 et 9
def get_player_choice(player):
    while True:
        try:
            position = int(input(f"Joueur {player}, choisissez une case entre 1 et 9 : "))
            if 1 <= position <= 9:
                return position
            print("Veuillez entrer un nombre entre 1 et 9.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Vérification si un joueur a gagné
def check_win(board, joueur):
    # Vérifie les lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            print(f"Joueur {joueur}, vous avez gagné!")
            return True

    # Vérifie les colonnes
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            print(f"Joueur {joueur}, vous avez gagné!")
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2]:
        print(f"Joueur {joueur}, vous avez gagné!")
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        print(f"Joueur {joueur}, vous avez gagné!")
        return True

    return False

# Vérification si c'est un match nul
def check_draw(board):
    for row in board:
        if any(cell not in ["X", "O"] for cell in row):  # Si une case n'est pas occupée
            return False
    print("C'est un match nul !")
    return True

# La fonction principale du jeu
def game():
    # Initialisation du plateau avec des numéros de 1 à 9
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    current_player = "X"  # Le joueur X commence

    while True:
        afficher_grille(board)  # Affiche l'état actuel du plateau
        position = get_player_choice(current_player)  # Demande le coup du joueur

        # Vérifie si la case est déjà occupée
        row = (position - 1) // 3
        col = (position - 1) % 3
        if board[row][col] in ["X", "O"]:
            print("Cette case est déjà occupée. Choisissez une autre case.")
            continue

        # Met à jour le plateau avec le choix du joueur
        update_board(board, position, current_player)

        # Vérifie si le joueur actuel a gagné
        if check_win(board, current_player):
            afficher_grille(board)
            break

        # Vérifie si le jeu est un match nul
        if check_draw(board):
            afficher_grille(board)
            break

        # Change de joueur
        current_player = "O" if current_player == "X" else "X"

# Lancer le jeu
game()
