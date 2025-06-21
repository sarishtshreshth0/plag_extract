n,x,y=map(int,input().split())
s= input()
c=0
d=x+y
e = 0
f= False
for i in range(n):
    if s[i]=="a":
        if c<d:
            f=True
    elif s[i]=="b":
        if c<d and e<y:
            f=True
            e+=1
    if f:
        print("Yes")
        c+=1
    else:
        print("No")
    f=False