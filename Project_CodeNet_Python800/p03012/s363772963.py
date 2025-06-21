n = int(input())
w = [int(x) for x in input().split()]
ans = 1e9
for i in range(n):
  s1 = sum(w[:i])
  s2 = sum(w[i:])
  s = abs(s1 - s2)
  ans = min(s, ans)
print(ans)