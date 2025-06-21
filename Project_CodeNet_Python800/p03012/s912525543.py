n=int(input())
W=list(map(int,input().split()))
ans = 1000000
for i in range(n):
  ans = min(ans,abs(sum(W[:i+1])-sum(W[i+1:])))
print(ans)