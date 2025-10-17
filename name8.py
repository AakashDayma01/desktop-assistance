a=int(input("enter a number: "))
mid=a//2
for i in range(0,a):
    for j in range(0,a):
        if(j==0 or j==(a-1) or i==mid):
            if(i==0 and j==0):
                print(" ",end=" ")
            print("*",end=" ")
            if(i==0 and j==0 ):
                for k in range(0,(a-3)):
                    print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

mid=a//2
for i in range(0,a):
    for j in range(0,a):
        if(j==0 or j==(a-1) or i==mid):
            if(i==0 and j==0):
                print(" ",end=" ")
            print("*",end=" ")
            if(i==0 and j==0 ):
                for k in range(0,(a-3)):
                    print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()
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
print()

mid=a//2
for i in range(0,a):
    for j in range(0,a):
        if(j==0 or j==(a-1) or i==mid):
            if(i==0 and j==0):
                print(" ",end=" ")
            print("*",end=" ")
            if(i==0 and j==0 ):
                for k in range(0,(a-3)):
                    print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

mid=a//2
for i in range(0,a):
    for j in range(0,a):
        if(j==0 or j==(a-1) or i==mid):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()