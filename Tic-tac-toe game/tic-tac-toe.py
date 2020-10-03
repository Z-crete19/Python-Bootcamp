# ic-tac-toe (American English) or Xs and Os, is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

import random

def display(board): # for displaying
    print(f"""
    {board[7]}|{board[8]}|{board[9]}                    7 | 8 | 9
    ---+---+---                   ---+---+---
    {board[4]}|{board[5]}|{board[6]}     Positions->    4 | 5 | 6
    ---+---+---                   ---+---+---
    {board[1]}|{board[2]}|{board[3]}                    1 | 2 | 3
     """)

def valid_input():
    while True:
        pos = input("Enter a Position: ")
        if pos != ' ': # if user press space the game ends
            if pos.isnumeric() and int(pos) in range(1, 10): # Check the position is numeric and also in range
                pos = int(pos)
                break
            print('Not a valid Position.')
        else:
            print("Thank You for playing Tic-tac-toe!")
            exit()
    return int(pos)


def valid_pos(turn, board):
    print(turn, 'chance')
    pos = valid_input()
    while True:
        if board[pos] == '   ':
            board[pos] = turn    
            break
        else:
            print("Cannot overwrite, Please select new location.")
            pos = valid_input()

def check(board):
    flag = 0
    # row
    if board[1] == board[2] == board[3] != '   ' or board[4] == board[5] == board[6] != '   ' or board[7] == board[8] == board[9] != '   ':
        flag = 1
    #column
    elif board[1] == board[4] == board[7] != '   ' or board[2] == board[5] == board[8] != '   ' or board[3] == board[6] == board[9] != '   ':
        flag = 1
    # diagonal
    elif board[1] == board[5] == board[9] != '   ' or board[3] == board[5] == board[7] != '   ':
        flag = 1

    return flag


def userInput(board, symbol):
    sym1, sym2 = symbol[random.randint(0,1)]
    print(sym1, "is going first\n\n")
    display(board)
    for i in range(9):
        if i % 2 == 0:
            turn = ' '+sym1+' '
            valid_pos(turn, board)
        else:
            turn = ' '+sym2+' '
            valid_pos(turn, board)

        display(board)

        if i >= 4:
            if check(board):
                display(board)
                print(turn, "Won.")
                break
        if i == 8:
            print("It\'s a tie, none won.")
            

    

def game():
    board = ["Just to adjust loc :)", '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '] 
    symbol = [('X', 'O'), ('O', 'X')]

    while True:
        marker = input("Enter your Marker (X/O): ").upper()
        if marker == 'X' or marker == 'O':
            print(marker)
            userInput(board, symbol)
            break
        else:
            print("Wrong Marker(X, O) please enter again.\n")

    #display(board)

def main():
    play = 'Y'
    while play == 'Y':
        print("Press [space] whenever you want to exit the game.\n\n\n")
        game()
        play = input("Wanna Play it again? (Y/N): ").upper()

if __name__ == "__main__":
    main() 






























