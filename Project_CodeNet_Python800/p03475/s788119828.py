N,*L = map(int, open(0).read().split())
ans = 0
inf = [0]*(N-1)
for i,(c,s,f) in enumerate(zip(*[iter(L)]*3)):
  inf[i] = (c,s,f)
for i in range(N-1):
  ans = 0
  for j in range(i,N-1):
    c,s,f = inf[j]
    m = ((ans-1)//f+1)*f
    ans = max(m,s)
    ans += c
  print(ans)
print(0)