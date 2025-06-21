from fractions import gcd
N,X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x = list(set(x))
x.sort()
y = [x[i+1]-x[i] for i in range(len(x)-1)]

if len(x) == 1:
  print(0)
  exit()
elif len(x) == 2:
  print(abs(x[1]-x[0]))
  exit()
else:
  ans = y[0]
  for i in range(len(y)):
    ans = gcd(ans,y[i])
print(ans)