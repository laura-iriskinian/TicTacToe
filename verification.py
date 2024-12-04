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
    if board[0][0] == board[1][1] == board[2][2] != "-":
        print(f"Joueur {player}, vous avez gagné!")
        return True
        
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




# Vérifier si le joueur actuel a gagné
    if check_win(board, player):
            print(f"Félicitations, joueur {player}! Vous avez gagné!")
            #break

        # Vérifier si la partie est nulle
    if check_draw(board):
            print("C'est un match nul!")
            #break