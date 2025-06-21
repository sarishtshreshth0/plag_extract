n,a,b=map(int,input().split())
MOD=10**9+7
def inv(a):
  return pow(a,MOD-2,MOD)
def choose(n,r):
  if r==0 or r==n:
    return 1
  else:
    A=B=1
    for i in range(r):
      A=A*(n-i)%MOD
      B=B*(i+1)%MOD
    return A*inv(B)%MOD
print((pow(2,n,MOD)-1-choose(n,a)-choose(n,b))%MOD)