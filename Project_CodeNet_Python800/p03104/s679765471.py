a,b=map(int,input().split())

def xorsum(x):
  if x % 4 == 1:
    return 1
  elif x % 4 == 3:
    return 0
  elif x % 4 == 0:
    return x
  else:
    return 1 ^ x

print(xorsum(b)^xorsum(a-1))