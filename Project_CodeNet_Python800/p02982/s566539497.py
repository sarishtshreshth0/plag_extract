n,d = map(int,input().split())
dots = []
ans = 0
for _ in range(n):
  t = list(map(int,input().split()))
  if len(dots)!=0:
    for l in dots:
      a = [(y-z)**2 for y,z in zip(t,l)]
      if ((sum(a))**.5).is_integer():
        ans += 1
  dots.append(t)
print(ans) 