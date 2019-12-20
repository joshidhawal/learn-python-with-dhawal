import random
computerScore=0
userScore=0
continuePlaying=1
Guide={1:"Stone",2:"Paper",3:"Scissor"}

#function to determine who wins and calculate the score
def game(user,computer):
    global computerScore
    global userScore
    if(user==computer):
        print("It's a tie, please play again.")
    elif(user==1 and computer==2):
        print("Computer Wins")
        computerScore+=1
    elif(user==1 and computer==3):
        print("User wins")
        userScore+=1
    elif(user==2 and computer==1):
        print("User wins")
        userScore+=1
    elif(user==2 and computer==3):
        print("Computer Wins")
        computerScore+=1
    elif(user==3 and computer==1):
        print("Computer Wins")
        computerScore+=1
    elif(user==3 and computer==2):
        print("User wins")
        userScore+=1


while(continuePlaying==1):
    #User takes a number from 1-3
    user=int(input("Enter your Choice\n1. Stone\n2. Paper\n3. Scissors\n"))
    #Now we will check for wrong inputs
    if(user>0 and user<4):
        #Now Computer will make a random choice from 1-3
        computer=random.randint(1,3)
        print("User: ",Guide[user],"Computer: ",Guide[computer])
        game(user,computer)
    else:
        print("Invalid Choice, Please Enter A Valid Choice")
        
    continuePlaying=int(input("Do you wish to Continue Playing?\nEnter 1 for Yes and 0 for No\n"))


print("The total scores are : ")
print("User :",userScore)
print("Computer :",computerScore)

if(userScore>computerScore):
    print("User Wins")
elif(computerScore>userScore):
    print("Computer Wins")
else:
    print("It's a tie")