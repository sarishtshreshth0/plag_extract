n = int(input())
w = list(map(int, input().split()))
ans = 1000
for i in range(n):
  ans = min(abs(sum(w[:i])-sum(w[i:])), ans)
print(ans)