n,a,b = map(int,input().split())
m = 10**9+7

def nCr(n_, r_, m_):
  c = min(r_ , n_ - r_)
  bunshi = 1
  bunbo = 1
  for i in range(1,c+1):
    bunshi = bunshi * (n_+1-i) % m_
    bunbo = bunbo * i % m_
  return bunshi * pow(bunbo, m_-2, m_) % m_


ans = pow(2,n,m)-1
ans -= nCr(n,a,m)
ans %= m
ans -= nCr(n,b,m)
ans %= m
print(ans)