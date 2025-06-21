a,b=map(int,input().split())
s=list(input())
f=0
for i in range(a):
    if not s[i] in "0123456789":
        f=1
if s[a]!="-":
    f=1
for i in range(b):
    if not s[i+a+1] in "0123456789":
        f=1
print("Yes" if f==0 else "No")
