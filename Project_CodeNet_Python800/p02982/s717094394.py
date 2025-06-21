N,D = map(int,input().split())
X = [list(map(int,input().split())) for n in range(N)]
a = 0

for i in range(N):
  for j in range(i):
    d = sum([(X[i][d]-X[j][d])**2 for d in range(D)])**0.5
    if d.is_integer():
      a+=1

print(a)