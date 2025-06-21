n,a,b=map(int,input().split())
mod=10**9+7

def pow(x, n):
  ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = ans*x%mod
    x = x*x%mod
    n = n >> 1 
  return ans

N=pow(2,n)
def comb(c,d):
  x=1
  for i in range(d):
    x=x*(c-i)%mod
  y=1
  for i in range(d):
    y=y*(i+1)%mod
  return x*pow(y,mod-2)%mod
A=comb(n,a)
B=comb(n,b)
print((N-A-B-1)%mod)