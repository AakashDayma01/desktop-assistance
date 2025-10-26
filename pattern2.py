#a=int(input("enter the length: "))
#for i in range(a):
 #   for k in range(1,i+1):
  #      print(end=" ")
   # for j in range(i,a):
    #    print("*",end=" ")
    #print()


#def fact(num):
 #   if num==0 or num==1:
  #      return 1
   # else:
    #    return num * int(fact(num-1))

#facto = fact(5)
#print(facto)

#num = int(input("enter a number: "))
#fact = 1
#for i in range(1,num+1):
 #   fact = fact*i
#print(fact)


l = [1,43,23,2,5,4,53]
l.sort()
start = 0
stop = len(l)-1
num = int(input("enter a number "))
for _ in range(len(l)-1):
    if start>stop:
        break
    mid = (start+stop)//2
    if l[mid] == num:
        print(f"number found at the index of {l.index(num)}")
        break
    elif num>l[mid]:
        start = mid+1
    elif num<l[mid]:
        stop = mid-1

