N, *L = map(int, open(0).read().split())
red = []
blue = []
for a, b in zip(*[iter(L[:2*N])]*2):
  red += [(a,b)]
for c, d in zip(*[iter(L[2*N:])]*2):
  blue += [(c,d)]
red.sort(reverse=True)
blue.sort(reverse=True)
S = set(range(N))

ans = 0
for a,b in red:
  k = -1
  m = 10**3
  for j, n in enumerate(blue):
    c,d = n
    if c<a:
      break
    if d-b>0 and d-b<m and j in S:
      k = j
      m = d-b
  if k!=-1:
    ans += 1
    S.remove(k)
print(ans)