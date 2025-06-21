S = list(input())
L = len(S)

ans = L
for m in range(2):
  t = 0
  for i in range(L):
    s = S[i]
    if i % 2 == m:
      if s == '0':
        t += 1
    else:
      if s == '1':
        t += 1
  ans = min(ans,t)
  
print(ans)