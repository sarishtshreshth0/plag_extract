a,b=map(int,input().split())
s=input()
n=len(s)
l=list("0123456789")

f=0
for i in range(a):
    if s[i] in l:
        f+=1
    
if s[a]=="-":
    
    f+=1

for i in range(b):
    if s[-1-i] in l:
        f+=1
    
print("Yes" if f==n else "No")

    
