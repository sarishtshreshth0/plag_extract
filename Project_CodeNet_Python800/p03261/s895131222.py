n=int(input())
w=input()
tmp=w[-1:]
d={}
d[w]=1
for i in range(1,n):
    w=input()
    if w not in d:
        d[w]=1
    else:
        print("No")
        exit()
    if w[0]==tmp:
        tmp=w[-1:]
    else:
        print("No")
        exit()
print("Yes")