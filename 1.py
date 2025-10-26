a=input("enter a string: ")
v=num=o=space=alpha=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in (a):
    if i in (vowels):
        v+=1
    elif(i>='0' and i<='9'):
        num+=1
    elif(i== " "):
        space+=1
    else:
        o +=1
print("no of vowels:",v ,"\n no of digits :",num,"\n no of other : ",o,"\n no of spaces: ",space)



