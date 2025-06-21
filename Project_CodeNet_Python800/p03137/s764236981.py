N, M=map(int, input().split())
X=list(map(int, input().split()))
X.sort()
if N>=M:
  print(0)
else:
  dif=[]
  for i in range(M-1):
    dif.append(X[i+1]-X[i])
  dif.sort(reverse=True)
  ans=sum(dif[N-1:])
  print(ans)