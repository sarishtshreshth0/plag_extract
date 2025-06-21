n=int(input())
a=l=list(map(int, input().split()))
ans=100000
Sum=sum(a)
cnt=0
for i in range(n):
  cnt+=a[i]
  ans=min(abs(Sum-2*cnt),ans)
print(ans)