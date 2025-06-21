def solve(N,K):
  if N == 0:
    return 1

  digit_num = 0
  while(1):
    if N >= pow(K,digit_num):
      digit_num += 1
    else:
      return digit_num
    
N, K = map(int,input().split())
ans = solve(N,K)
print(ans)