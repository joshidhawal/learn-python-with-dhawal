''' Program to print pattern
   * 
  * * 
 * * * 
* * * *
'''

for i in range(1,5):
    for j in range(1,5-i):
        print (end=' ')
    for j in range (1,i+1):
        print ('*', end=" ")
    print()
