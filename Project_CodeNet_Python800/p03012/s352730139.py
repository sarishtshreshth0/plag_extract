n = int(input())
w = list(map(int, input().split()))

ans = sum(w)
for i in range(n):
  s1 = sum(w[:i+1])
  s2 = sum(w[i+1:n])
  ans = min(ans, abs(s2-s1))
  
print(ans)