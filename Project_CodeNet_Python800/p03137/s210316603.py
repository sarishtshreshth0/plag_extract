N,M=map(int,input().split())
X=list(map(int,input().split()))

if N>=M:
  print(0)
  exit()

X = sorted(X)

diff=[]
for i in range(1,M):
  diff.append(X[i]-X[i-1])

diff = sorted(diff)
print(sum(diff[:M-N]))