n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
def POW(x, y):
  bin_ = []
  while y:
    bin_.append(y % 2)
    y >>= 1
  ret = 1
  for j in reversed(bin_):
    ret = (ret * ret) % mod
    if j == 1:
      ret = (ret * x) % mod
  return ret
def comb(x, y):
  ret = 1
  for i in range(1, y+1):
    ret = (ret * (x+1-i)) % mod
    ret = (ret * POW(i, mod-2)) % mod
  return ret
print((POW(2, n) - 1 - comb(n, a) - comb(n, b)) % mod)