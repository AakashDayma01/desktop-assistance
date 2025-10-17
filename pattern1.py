a= int(input("enter athe length of pyramid: "))
for i in range (1,a+1):
    for k in range(i,a):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end=" ")
    print( )
for l in range(1,a+1):
    for b in range(1,l+1):
        print(end = " ")
    for c in range(l,a):
        print("*",end=" ")
    print( )