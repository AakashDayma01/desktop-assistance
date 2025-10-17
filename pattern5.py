a=int(input("enter a number: "))
for i in range(1,a):
    for j in range(0,i*2):
        print(end=" ")
    for k in range(i,a):
        print("*",end=" ")
    print()