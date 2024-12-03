board = []
for row in range (3):
    board.append([])
    for column in range (3):
        board [row].append('-')

def print_board(board):
    for row in board:
        print (" ".join(row))
        print("-" * 5)
print_board(board)



def demander_coup(self):
    while True:
        try:
            ligne = int(input(f"{self.joueur_actuel}, entrez le numéro de la ligne (0-2) : "))
            colonne = int(input(f"{self.joueur_actuel}, entrez le numéro de la colonne (0-2) : "))
            if self.valider_coup(ligne, colonne):
                return ligne, colonne
        except ValueError:
            print("Veuillez entrer des nombres entiers entre 0 et 2.")
        else:
            print("Coordonnées invalides ou case déjà occupée.")

board = []
for row in range (3):
    board.append([])
    for column in range (3):
        board [row].append('-')

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)