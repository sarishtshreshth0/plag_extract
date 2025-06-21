N=int(input())
weight=list(map(int,input().split()))
ans=1000
for i in range(N):
    sa=abs(sum(weight[:i+1])-sum(weight[i+1:]))
    if sa<ans: ans=sa
print(ans)
