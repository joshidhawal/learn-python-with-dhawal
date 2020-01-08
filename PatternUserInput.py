''' Program to print the pattern taking the user input
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   *
'''
num=int(input("Enter the number from 1-10: "))
num=num+1
for i in range(1,num):
    for j in range(1,num-i):
        print (end=' ')
    for j in range (1,i+1):
        print ('*', end=" ")
    print()
for i in range(1,num):
    for j in range(1,1+i):
        print (end=' ')
    for j in range (1,num-i):
        print ('*', end=" ")
    print()