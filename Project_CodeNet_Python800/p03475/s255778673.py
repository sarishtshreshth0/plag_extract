n = int(input())
C = []
S = []
F = []
for _ in range(n-1):
  c,s,f = map(int, input().split())
  C.append(c)
  S.append(s)
  F.append(f)

for i in range(n-2):
  ans = C[i]+S[i]
  for j in range(i+1, n-1):
    if S[j] >= ans:
      ans += (S[j]-ans) + C[j]
    else:
      if (ans-S[j])%F[j] == 0: ans += C[j]
      else: ans += F[j] - (ans-S[j])%F[j] + C[j]
  print(ans)
print(C[-1]+S[-1])
print(0)