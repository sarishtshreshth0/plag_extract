N, K = map(int, input().split())
ans = 0
num = 1

while num <= N:
  num *= K
  ans += 1
  
print(ans)