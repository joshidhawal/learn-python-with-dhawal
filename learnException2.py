try :
    a=int(input("Divide 10 by : "))
    if (a<0):
        raise Exception("Enter anything else please!")
    b=10
    a=b/a
    print(a)
except ZeroDivisionError :
    print("You can't divide by zero, enter a valid number again")
    a=int(input("Divide 10 by : "))
    b=10
    a=b/a
    print(a)
except Exception as e:
    print("Some error occured\nError Description : "+str(e))
finally:
    print("Sorry, run the program again")    
    