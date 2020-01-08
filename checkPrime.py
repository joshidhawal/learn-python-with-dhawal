def checkPrime(n):
    '''to check if the number is prime or not.
    We will use the basic test of divisibility from mathematics.'''
    if(n==2 or n==3 or n== 5 or n==7 ):
        return True
    elif(n%2==0):
        return False
    elif(n%3==0):
        return False
    elif(n%5==0):
        return False
    elif(n%7==0):
        return False
    else:
        return True
       
n=int(input("Enter Any Integer from 2-100\n"))

result=checkPrime(n)

if(result==True):
    print(n," is a prime number.")
else:
    print(n," is not a prime number.")