N = int(input())
CSF = [list(map(int, input().split())) for i in range(N-1)]

ans = []
for i, (ci, si, fi) in enumerate(CSF):
  now = si + ci
  for j in range(i+1, N-1):
    cj, sj, fj = CSF[j]
    now = max((-(-now//fj))*fj, sj) + cj
  ans.append(now)

ans.append(0)
print(*ans, sep='\n')