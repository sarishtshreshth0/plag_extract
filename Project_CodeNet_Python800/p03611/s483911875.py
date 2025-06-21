def solve():
  ans = 0
  N = int(input())
  A = list(map(int, input().split()))
  lis = [0]*(10**5+2)
  for i in range(N):
    lis[A[i]-1] += 1
    lis[A[i]] += 1
    lis[A[i]+1] += 1
  ans = max(lis)
  return ans
print(solve())