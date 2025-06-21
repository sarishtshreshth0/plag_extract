a,b=map(int,input().split())
def f(x):
  r=x%2^x//2%2
  p=2
  for i in range(len(bin(x))-3):
    r+=p-p*(x%2 or x%(p*2)<p)
    p*=2
  return r
print(f(a-1)^f(b))