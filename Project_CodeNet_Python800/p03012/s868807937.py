n = int(input())
W = list(map(int, input().split()))
S = sum(W)

ans = abs(W[0] - (S - W[0]))
for i in range(1,n):
  k = abs(sum(W[0:i+1]) - (S - sum(W[0:i+1])))
  if k > ans:
    print(ans)
    exit()
  else:
    ans = k