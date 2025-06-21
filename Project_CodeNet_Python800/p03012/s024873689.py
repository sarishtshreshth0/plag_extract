n = int(input())
w = list(map(int,input().split()))
ans = abs(sum(w[0:1]) - sum(w[1:n+1]))
for i in range(1,n-1):
  a = abs(sum(w[0:i+1]) - sum(w[i+1:n+1]))
  ans = min(ans,a)
print(ans)