n,k = map(int, input().split())

ans = 0

while n > 0:
  n /= k
  n = int(n)
  ans += 1
  
print(ans)
