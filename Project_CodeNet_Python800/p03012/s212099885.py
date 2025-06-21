N=int(input())
W=list(map(int, input().split()))
 
sum1,sum2=0,0
ans=0
dif=1000
 
for i in range(N):
    sum1=sum(W[0:i])
    sum2=sum(W[i:])
    now = abs(sum1-sum2)
    if dif > now:
        dif =now
 
print(dif)