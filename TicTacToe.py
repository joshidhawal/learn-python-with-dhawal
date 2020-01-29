"""
This Program is to play Tic Tac Toe game in CLI

"""
def showBoard(board):
    # this will print the current status of the board,
    # this is not needed in plain way but it's just,
    # here to make this look fancy.
    print("The present status of the board is :")
    for i in range(3):
        print("----------\n|",end="")
        for j in range(3):
            print(board[i][j], end=" |")
        print("")
    print("----------")

def playOnBoard(player,line):
    # This will run the loop letting the assigned player,
    # play until the winning condition is met.
    while(line!=True):
        showBoard(board_help)
    pos=int(input("Enter the position where you'd like to enter the symbol : "))
    a=dict(pos)
    if(board[a[0]][a[1]]!=player1 or board[a[0]][a[1]]!=player2):
        board[a[0]][a[1]]=player
    line=lineCheck()
    showBoard(board)

def lineCheck():
    ## This will check if the winning conditions are true.
    if (board[0][0]==board[0][1] and board[0][1]==board[0][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True 
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2]):
        return True
    else :
        return False
        


board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
board_help=[['1','2','3'],['4','5','6'],['7','8','9']]
player1='X'
player2='O'
#player1=input("Enter the Symbol you want to use for player1 : ")
#player2=input("Enter the Symbol you want to use for player2 : ")

print("Player 1 will use : "+player1+" and Player 2 will use : "+player2)
dict={1:[0,0],2:[0,1],3:[0,2],
      4:[1,0],5:[1,1],6:[1,2],
      7:[2,0],8:[2,1],9:[2,2]}
showBoard(board)
line=False


