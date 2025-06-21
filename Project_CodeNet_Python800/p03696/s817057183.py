n=int(input())
s=input()

now=0
sen=0

for i in range(n):
    if s[i]=="(":
        now+=1
    else:
        now-=1
    if now==-1:
        sen+=1
        now=0

print("("*sen + s + ")"*now)