M,D = map(int,input().split())
cnt = 0
if D > 21 and M > 3:
  for m in range(4,M+1):
    for d in range(22,D+1):
      a,b = divmod(d,10)
      if a > 1 and b > 1:
        if m == a*b:
          cnt += 1
      
print(cnt)