n,a,b = tuple(map(int,input().split()))

s = list(input())
rank = 0
brank = 0
for s_i in s:
  if s_i=='a':
    if rank==a+b:
      print("No")
      continue
    rank+=1
    print("Yes")
  elif s_i=='b':
    if rank==a+b:
      print("No")
      continue
    if brank==b:
      print("No")
      continue
    rank+=1
    brank+=1
    print("Yes")
  else:
    print("No")