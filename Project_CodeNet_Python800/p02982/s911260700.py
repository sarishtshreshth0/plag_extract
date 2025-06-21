N,D = map(int,input().split())
P = [list(map(int,input().split())) for i in range(N)]
count = 0
for i in range(N-1):
  for j in range(i+1,N):
    x = 0
    for k in range(D):
      x += abs(P[i][k] - P[j][k])**2
    ans = x**(1/2)
    if ans.is_integer():
      count += 1
print(count)