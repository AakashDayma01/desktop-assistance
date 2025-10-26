a= int(input("enter athe length of pyramid: "))
for i in range (1,a+1):
    for k in range(i,a):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end=" ")
    print()