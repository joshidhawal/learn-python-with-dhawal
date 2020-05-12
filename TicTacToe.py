"""
This Program is to play Tic Tac Toe game in CLI

"""
import os
from os import system,name
from time import sleep

def clearScreenOutput():
    #sleep(5)
    #for windows
    if name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def checkBoardFill():
    fill = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]==player1 or board[i][j]==player2:
                    fill=fill+1
    
    if fill==9:
        return True
    else:
        return False

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
    print("----------\n")

def playOnBoard(boardIndexHelp,player):
    # This will run the loop letting the assigned player,
    # play until the winning condition is met.
    notPlayed = True
    while (notPlayed):
        
        print("Reference Board for Index Position : ")
        showBoard(board_help)
        pos=int(input("Enter the position where you'd like to enter the symbol : "))
        clearScreenOutput()
        #add method to check for a valid position or not.
        a=boardIndexHelp[pos]
        try:
            if((board[a[0]][a[1]]!=player1 and board[a[0]][a[1]]==' ') or (board[a[0]][a[1]]!=player2 and board[a[0]][a[1]]==' ')):
                board[a[0]][a[1]]=player
                notPlayed = False
                print("The Current Board Status is : ")
                showBoard(board)
                print("\n--------------------------------------------------\n")
            else :
                # Gives invalid position prompt
                # when there's already another player's
                # input on the position
                print("That position is already occupied,Enter a valid position")
                notPlayed=True
        except Exception as e :
            print("Enter a valid position \n The Error is : "+e)
            notPlayed=True

    
def lineCheck(line):
    ## This will check if the winning conditions are true.
    if (board[0][0]==board[0][1] and board[0][1]==board[0][2]and board[0][0]==board[0][2] and board[0][2]!=' '):
        return False
    elif (board[1][0]==board[1][1] and board[1][1]==board[1][2] and board[1][0]==board[1][2] and board[1][2]!=' '):
        return False
    elif (board[2][0]==board[2][1] and board[2][1]==board[2][2] and board[2][0]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[0][0]==board[1][0] and board[1][0]==board[2][0] and board[0][0]==board[2][0] and board[2][0]!=' '):
        return False
    elif (board[0][1]==board[1][1] and board[1][1]==board[2][1] and board[0][1]==board[2][1] and board[2][1]!=' '):
        return False
    elif (board[0][2]==board[1][2] and board[1][2]==board[2][2] and board[0][2]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]==board[2][2] and board[2][2]!=' '):
        return False
    elif (board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]==board[0][2] and board[0][2]!=' '):
        return False
    else:
        return True
    
        


board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
board_help=[['1','2','3'],['4','5','6'],['7','8','9']]
player1=input("Enter the Symbol you want to use for player1 : ") 
player2=input("Enter the Symbol you want to use for player2 : ")
#player1='X'
#player2='O'

print("Player 1 will use : "+player1+" and Player 2 will use : "+player2)

clearScreenOutput()

boardIndexHelp={1:[0,0],2:[0,1],3:[0,2],
      4:[1,0],5:[1,1],6:[1,2],
      7:[2,0],8:[2,1],9:[2,2]}
print("The Game Board is initialised")
showBoard(board)
line = True
previousPlayer=player2
while(line):
    
    if previousPlayer==player2:
        print("\nPLAY : PLAYER "+player1)
        playOnBoard(boardIndexHelp,player1)
        previousPlayer=player1
        line = lineCheck(line)
        if line==False:
            print("The Winner is : "+player1)
    else:
        print("\nPLAY : PLAYER "+player2)
        playOnBoard(boardIndexHelp,player2)
        line = lineCheck(line)
        previousPlayer=player2
        if line==False:
            print("The Winner is : "+player2)

    tie = checkBoardFill()
    if (tie == True and line == True):
        print("Game Over it's a tie")
        line=False
