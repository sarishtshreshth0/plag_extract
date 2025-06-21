N, X = map(int, input().split())
x_list=list(int(x)-X for x in input().split())

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

ans=0
for x in x_list:
  ans=gcd(ans, x)
print(abs(ans))


