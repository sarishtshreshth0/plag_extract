n = int(input())
w = list(map(int, input().split()))
ans = 100000000

for i in range(n+1):
  # print(sum(w[:i]), sum(w[i:]))
  tmp = abs(sum(w[:i])-sum(w[i:]))
  if ans > tmp:
    ans = tmp
print(ans)