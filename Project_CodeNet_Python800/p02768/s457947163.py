mod = 10**9+7
def cmb(x, y):
  ret = 1
  for i in range(1, y+1):
    ret = (ret * (x+1-i)) % mod
    ret = (ret * pow(i, mod-2, mod)) % mod
  return ret

n,a,b = map(int,input().split())
ans = (pow(2,n,mod) - 1 - cmb(n,a) - cmb(n,b)) % mod
print(ans)