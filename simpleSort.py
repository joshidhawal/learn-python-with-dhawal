def sorting(a,l):
    for i in a:
        for i in range (1,l):
            if(a[i-1]>a[i]):
                t=a[i-1]
                a[i-1]=a[i]
                a[i]=t


l=int(input("Enter the size of list you want to sort.\n"))
t=0
a=[]
for i in range (l):
    a.append(int(input("Enter the element in list.\n")))
print ("This is your entered list : ",a)
sorting(a,l)
print ("This is your sorted list : ",a)
