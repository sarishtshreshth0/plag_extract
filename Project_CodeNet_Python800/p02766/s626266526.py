N, K = map(int, input().split())
 
ans = 1
while 1:
  if N >= K ** ans:
    ans += 1
    continue
  else:
    print(ans)
    break