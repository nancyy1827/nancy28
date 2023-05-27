file=open("nancy.txt","w")
file.write("this is prg")
print("hi..")

file.close()

file=open("nancy.txt","r")
print(file.read())
file.close()


file=open("nancy.txt","a")
file.write("this is extra")
file.close()

file=open("nancy.txt","r")
print(file.read())
file.close()


file=open("nancy.txt2","w+")
file.write("this file is both r nd w")
print(file.tell())
file.seek(0)
print(file.read())
file.close()

file=

