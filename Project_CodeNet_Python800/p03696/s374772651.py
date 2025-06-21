n=int(input())
s=input()
cntl=0
for i in range(n-1,-1,-1):
    if s[i]==")":
        cntl+=1
    elif s[i]=="(" and cntl>0:
        cntl-=1
sl="("*cntl
cntr=0
for i in range(n):
    if s[i]=="(":
        cntr+=1
    elif s[i]==")" and cntr>0:
        cntr-=1
sr=")"*cntr
print(sl+s+sr)
