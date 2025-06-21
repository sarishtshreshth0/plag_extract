N,M = map(int, input().split())
X = list(map(int,input().split()))
if N >= M:
  print(0)
else:
  X = sorted(X)
  list = [X[i]-X[i-1] for i in range(1,M)]
  list = sorted(list)
  list1 = list[:M-N]
  print(sum(list1))