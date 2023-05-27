a=input("enter a string=")
b=len(a)
if(b<3):
    print("can't change")
else:
    if(a.endswith("ing")):
        s=a.replace("ing","ly")
        print(s)
    else:
        print(a+"ing")
