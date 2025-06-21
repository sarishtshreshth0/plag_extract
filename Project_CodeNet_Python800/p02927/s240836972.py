M, D = map(int,input().split())
if D<22:
  print(0)
else:
  count = 0
  for i in range(22,D+1):
    d1 = i%10
    d10 = (i-d1)//10
    if d1>1 and d10>1 and d1*d10 <= M:
      count+=1
  print(count)