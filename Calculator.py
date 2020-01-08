
#creating an addition function
def addition (a,b):
    a=a+b
    print ("The result of addition is ",a)
   
#creating a subtraction function
def subtraction (a,b):
    a=a-b
    print ("The result of subtraction is ",a)
   
#creating a multiplication function
def multiplication (a,b):
    a=a*b
    print ("The product is ",a)
   
#creating a division function
def division (a,b):
    a=a/b
    print ("The quotient after divsion is ",a)

#creating a modulus division function
def moddiv (a,b):
    a=a%b
    print ("The remainder after division is ",a)

#Once we are done with Creating functions
# First we would need to make a variable to see if the program should run again or not once an operation is finished.
choice=1

#Putting 1 or 0 inside conditions means telling the condition is true or false respectively.
while(choice):
    #take both input numbers
    a=int(input("Enter the a "))
    b=int(input("Enter the b "))
    #printing both numbers
    print("The a is ",a," and b is ",b)
    #now we have taken a variable which will let user enter the choice again if he/she had entered a wrong option.
    run_loop=1
    #since the default value of run_loop is kept 1 it will mean true and while loop will run

    while(run_loop):
        #take the choice from the user what what operation they want to peform.
        c=int(input("Enter the correct number for the operation you want to perform.\n1. Addition (a+b)\n2. Subtraction (a-b)\n3. Multiplication (a*b)\n4. Division (a/b)\n5.Modulus Divison (a%b)\n"))
        print ("You chose option number ",c)
        if(c==1):
            #a function is called depending on the choice made
            addition(a,b)
            #making run_loop 0 means next time it won't run while loop and it will get out of this while loop.
            run_loop=0
        elif(c==2):
            subtraction(a,b)
            run_loop=0
        elif(c==3):
            multiplication(a,b)
            run_loop=0
        elif(c==4):
            division(a,b)
            run_loop=0
        elif(c==5):
            moddiv(a,b)
            run_loop=0
        else:
            #we haven't made any run_loop changes as we want user to enter the valid choice again for the same set of numbers.
            print("sorry invalid input, enter the correct choice again.")

    #once the operation is over, we can ask user if they want to do more calculations or just end the program.
    choice=int(input("Enter 1 to continue and 0 to end the program\n"))
#This will print a thanks note and end the program.
print ("Thank You for Using our calculator program, you'd need to run the program again to perform more calculations.")