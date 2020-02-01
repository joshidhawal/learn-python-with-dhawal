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

def playOnBoard(player):
    # This will run the loop letting the assigned player,
    # play until the winning condition is met.
    showBoard(board_help)
    played=False
    pos=int(input("Enter the position where you'd like to enter the symbol : "))
    #add method to check for a valid position or not.
    try:
        a=dict(pos)
        if(board[a[0]][a[1]]!=player1 or board[a[0]][a[1]]!=player2):
            board[a[0]][a[1]]=player
            played = True
        else :
            # Gives invalid position prompt
            # when there's already another player's
            # input on the position
            print("That position is already occupied,
            Enter a valid position")
    except:
        print("Enter a valid position")
        line=lineCheck()
    showBoard(board)

def lineCheck():
    ## This will check if the winning conditions are true.
    
        


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


