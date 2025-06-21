#HarshadNumber
n = int(input())
def hrsh(x):
  s = 0
  while x > 10:
    s += x % 10
    x = x//10
  s += x
  return s
f = hrsh(n)
#print(f)
if n % f == 0:
  print('Yes')
else:
  print('No')