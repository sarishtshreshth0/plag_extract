def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
 
def lcm(a, b):
  return a*b // gcd(a, b)

N = int(input())
ans = lcm(2, N)
print(ans)
