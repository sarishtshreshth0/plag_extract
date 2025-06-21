a,b=map(int,input().split())
s=input()
t=True
if s[a]=="-":
    x,y=s[:a],s[a+1:]
    if "-" in x or "-" in y:
        t=False
else:
    t=False
print("Yes" if t else "No")