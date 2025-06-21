N=int(input())
D=list(map(int,input().split()))
MOD=998244353
goal=-1
tree=[0]*(N)
ans=1
for i in range(N):
    a=D[i]
    goal=max(a,goal)
    tree[a]+=1
if tree[0]==1 and D[0]==0:
    for i in range(1,goal+1):
        ans*=pow(tree[i-1],tree[i],MOD)
        ans%=MOD
    print(ans)
else:
    print(0)