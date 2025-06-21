N=int(input())
W=list(map(int,input().split()))

ans=10000000000000000
for t in range(N):
    sum1=0
    sum2=0
    for j in range(0,t+1):
        sum1+=W[j]
    for k in range(t+1,N):
        sum2+=W[k]
    if abs(sum2-sum1)<ans:
        ans=abs(sum2-sum1)
print(ans)
