n, a, b = map(int, input().split())
p = 10**9 + 7
def comb(n, r, p):
  X, Y = 1, 1
  for i in range(r):
    X *= n-i
    Y *= i+1
    X %= p
    Y %= p
  return int(X * pow(Y, p-2, p))
ans = pow(2, n, p) - comb(n, a, p) - comb(n, b, p) - 1
print(ans % p)