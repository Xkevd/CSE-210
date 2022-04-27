#Kevin del Hoyo

def main():
    board=[]
    print_board(board)
    current_player = input("Are you playing with 'x' or 'o'? ")
    while not (winner(board) or a_draw(board)):
        index = input(f"Put the '{current_player}' on the spot number: ")
        change_board(board, index, current_player)
        print_board(board)
        current_player = next_player(current_player)
    if a_draw(board):
        print("It's a draw")
    elif winner(board):
        print(f"Congratulations the '{next_player(current_player)}' won")

    pass

def change_board(board, index, player):
    board[int(index)-1] = player.lower()
    
    pass
def print_board(board):
    for i in range(9):
        board.append(i + 1) 
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")

    pass
def winner(board):
    return(board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def next_player(current_player):
    if current_player.lower() == "x":
        return "o"
    else:
        return "x"

def a_draw(board):
    if not winner(board):
        if board.count("x")>4 or board.count("o")>4:
            return True
    

if __name__ == "__main__":
    main()