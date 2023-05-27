n=["paython","ya","n","mis","cyyyyy"]
long=len(n[0])
word=n[0]
for i in n:
    if(len(i)>long):
        long=len(i)
        word=i
print(long,"longest length")
print(word,"longest word")
