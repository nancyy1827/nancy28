s=input("enter the string=")
alpha=0
for i in s:
    if(i.isalpha()):
        alpha+=1
        print("total character=",alpha)
