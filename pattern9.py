a=int(input("enter a number: "))
mid=a//2
d=mid-1
c=mid+2
for i in range(0,a):
    c-=1
    for j in range(0,a):
        if(i>0 and i<mid):
            if(j==c):
                print("*",end=" ")
        if(j==0 or j==i-d):
            print ("*",end=" ")
        elif(i==mid+1 and j==2):
            print(" ",end=" ")
        else:
            print(" ",end=" ")
    print()