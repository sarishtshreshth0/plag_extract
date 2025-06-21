n = int(input())
w = list(map(int, input().split()))
res = 10 ** 5
for i in range(0, n-1):
  a = abs(sum(w[:i+1]) - sum(w[i+1:]))
  if a < res:
    res = a
print(res)