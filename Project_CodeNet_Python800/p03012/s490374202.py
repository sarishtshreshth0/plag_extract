N = int(input())
W = list(map(int,input().split()))
ans = 1000000
for i in range(N):
  num = abs(sum(W[:i])-sum(W[i:]))
  ans = min(num,ans)
print(ans)