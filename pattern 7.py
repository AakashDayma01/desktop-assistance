a=int(input("enter a number: "))
for i in range(0,a):
    for j in range(0,a):
        if(j==0 or j==i or i==(a-1)):
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print()
