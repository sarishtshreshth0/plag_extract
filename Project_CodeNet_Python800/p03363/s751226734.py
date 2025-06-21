N=int(input())
A=list(map(int,input().split()))

temp=0
S=[0]
for i in range(N):
    S.append(S[i]+A[i])
S.sort()

D={}
for j in range(N):
    if S[j]==S[j+1]:
        if S[j] in D:
            D[S[j]]+=1
        else:
            D[S[j]]=2

ans=0
for d in D:
    if D[d]>1:
        ans+=D[d]*(D[d]-1)//2
print(ans)