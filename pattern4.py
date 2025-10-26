num=int (input("enter a number: "))
k=0
for i in range(1,num+1):
    mid=num//2
    a=(mid)+1
    if(i<=(mid+1)):
        k+=1
    else:
        k-=1
    for j in range(1,num+1):
        if(j<=(a+1-k) or j>=(mid+k)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

        


