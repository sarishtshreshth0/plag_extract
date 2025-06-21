a,b = map(int,input().split())

def sum_xor(x):
  if x%2!=0:
    if (x+1)/2%2==0:
      return 0
    else:
      return 1
  else:
    a = 0
    if ((x)//2)%2==0:
      a = 0
    else:
      a = 1
    return a^x

c = sum_xor(b)
d = sum_xor(a-1)
print(c^d)