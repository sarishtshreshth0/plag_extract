N=int(input())
S=list(input())

count=0
LR=[0,0]
for i in range(N):
    if S[i]=="(":
        count+=1
    else:
        if count==0:
            LR[0]+=1
            continue
        count-=1

LR[1]=count
for i in range(2):
    for j in range(LR[i]):
        if i==0:
            S.insert(0,"(")
        else:
            S.append(")")

print("".join(S))