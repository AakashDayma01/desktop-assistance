a= int(input("enter a number: "))
for i in range(0,a):
    for j in range(0,a):
        if(i==0 or i>=(a-1)):
            print("*",end=" ")
        elif(j==0 or j==(a-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()