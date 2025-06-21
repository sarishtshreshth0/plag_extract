a,b = map(int,input().split())

n = b - a + 1


if n % 2 == 0:
  if a % 2 == 1:
    ans = a ^ (((n - 2) // 2) % 2) ^ b
  else:
    m = n // 2
    ans = (m + 1) % 2 ^ 1
else:
  nn = (n - 1) // 2
  if a % 2 == 1:
    ans = (nn % 2) ^ a
  else:
    ans = (nn % 2) ^ b
    
print(ans)