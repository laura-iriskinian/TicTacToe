joueur = "X"
joueur = "O"
def check_win (board, joueur):
    #Verifié des lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            print(f"Joueur {joueur}, vous avez gagné!")
            return True

    #Verifié des colonnes
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            print(f"Joueur {joueur}, vous avez gagné!")
            return True
        
    #Verifié des diagonales
    if board[0][0] == board[1][1] == board[2][2] != "-":
        print(f"Joueur {joueur}, vous avez gagné!")
        return True
        
    if board[0][2] == board[1][1] == board[2][0] != "-":
        print(f"Joueur {joueur}, vous avez gagné!")
        return True
    
    return None

# Vérification si c'est un match nul
def check_draw(board):
    for row in board:
        if "-" in row:
            return False
    print("C'est un tirage au sort. Essayez à nouveau")
    return True
    
# Changement de joueur
#joueur_actuel = "O" if joueur_actuel == "X" else "X"