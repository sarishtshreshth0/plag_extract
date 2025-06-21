def solve():
  N, M = map(int, input().split())
  X = list(map(int, input().split()))
  X.sort()
  lis = []
  for i in range(M-1):
    lis.append(X[i+1]-X[i])
  lis.sort(reverse=True)
  ans = X[-1]-X[0]-sum(lis[:N-1])
  return ans
print(solve())