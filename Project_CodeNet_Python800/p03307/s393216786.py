N=int(input())
def gcd(a,b):
  if a==b:
    return a
  else:
    a,b=max(a,b),min(a,b)
    if a%b==0:
      return b
    return gcd(b,a%b)  
if N%2==0:
  print(N)
else:
  lcm=int(2*N/gcd(2,N))
  print(lcm)