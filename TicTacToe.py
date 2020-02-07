"""
This Program is to play Tic Tac Toe game in CLI

"""
def showBoard(board):
    # this will print the current status of the board,
    # this is not needed in plain way but it's just,
    # here to make this look fancy.
    # print("The present status of the board is :")
    for i in range(3):
        print("----------\n|",end="")
        for j in range(3):
            print(board[i][j], end=" |")
        print("")
    print("----------")

def playOnBoard(boardIndexHelp,player):
    # This will run the loop letting the assigned player,
    # play until the winning condition is met.
    notPlayed = True
    while (notPlayed):
        showBoard(board_help)
        pos=int(input("Enter the position where you'd like to enter the symbol : "))
        #add method to check for a valid position or not.
        print ("The entered Position is : "+str(pos))
        a=boardIndexHelp[pos]
        print(a)
        try:
            if(board[a[0]][a[1]]!=player1 or board[a[0]][a[1]]!=player2):
                board[a[0]][a[1]]=player
                notPlayed = False
                showBoard(board)
            else :
                # Gives invalid position prompt
                # when there's already another player's
                # input on the position
                print("That position is already occupied,Enter a valid position")
        except Exception as e :
            print("Enter a valid position \n The Error is : "+e)
        return notPlayed

    
def lineCheck(line):
    ## This will check if the winning conditions are true.
    if (board[0][0]==board[0][1] and board[0][1]==board[0][2] and board[0][2]!=' '):
        return False
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2] and board[1][2]!=' '):
        return False
    elif (board[2][0]==board[2][1] and board[2][1]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[0][0]==board[1][0] and board[1][0]==board[2][0] and board[2][0]!=' '):
        return False
    elif (board[0][1]==board[1][1] and board[1][1]==board[2][1] and board[2][1]!=' '):
        return False
    elif (board[0][2]==board[1][2] and board[1][2]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[0][2]!=' '):
        return False
    else:
        return True
    
        


board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
board_help=[['1','2','3'],['4','5','6'],['7','8','9']]
player1=input("Enter the Symbol you want to use for player1 : ")
player2=input("Enter the Symbol you want to use for player2 : ")

print("Player 1 will use : "+player1+" and Player 2 will use : "+player2)
boardIndexHelp={1:[0,0],2:[0,1],3:[0,2],
      4:[1,0],5:[1,1],6:[1,2],
      7:[2,0],8:[2,1],9:[2,2]}
print("The Game Board is initialised")
showBoard(board)
line = True
previousPlayer=player2
while(line):
    if previousPlayer==player2:
        playOnBoard(boardIndexHelp,player1)
        line = lineCheck(line)
        previousPlayer=player1
        if line==False:
            print("The Winner is : "+player1)
    else:
        playOnBoard(boardIndexHelp,player2)
        line = lineCheck(line)
        previousPlayer=player2
        if line==False:
            print("The Winner is : "+player1)



