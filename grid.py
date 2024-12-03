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
    elif move == "2":
        board[2][8] = player
    elif move == "9":
        board[2][2] = player
    else: 
        print(f"Mouvement {move} invalide")

board = create_board()
print_board(board)


## exemple pour pouvoir jouer --> boucle à créer

player = "X"
user_move(board,player)
print_board(board)

player = "O"
user_move(board,player)
print_board(board)