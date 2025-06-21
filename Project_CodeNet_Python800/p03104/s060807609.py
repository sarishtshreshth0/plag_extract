a,b=map(int,input().split())
def xor_sum(x):
  r=x%2^x//2%2
  p=2
  for i in range(len(bin(x))-3):
    r+=p*(x%2<1 and x%(p*2)>=p)
    p*=2
  return r
print(xor_sum(a-1)^xor_sum(b))