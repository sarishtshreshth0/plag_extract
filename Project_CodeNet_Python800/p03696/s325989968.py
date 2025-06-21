n=int(input())
s=input()
a=0
x=""
y=""
for i in range(n):
    if s[i]=="(":
        a+=1
    else:
        a-=1
if a>0:
    s=s+")"*a
elif a<0:
    s="("*abs(a)+s
#print(s)
t=0

while t==0:
    b=0
    for i in range(len(s)):
        if s[i]=="(":
            b+=1
        else:
            b-=1
        if b<0:
            s="("+s+")"
            #print(s)
            break
    if b==0:
        break
print(s)