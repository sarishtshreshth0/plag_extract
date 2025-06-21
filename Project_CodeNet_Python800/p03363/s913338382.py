N=int(input())
A=list(map(int,input().split()))

S=[]
S.append(0)
for i in range(N):
    S.append(S[i]+A[i])

x=dict()
for i in range(len(S)):
    s=S[i]
    if s in x:
        x[s]+=1
    else:
        x[s]=1
ans=0
#print(S)
#print(x)
for idx in x:
    ans+=((x[idx]-1)*(x[idx]))//2
print(ans)