N = int(input())

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

print(N*2//gcd(N, 2))