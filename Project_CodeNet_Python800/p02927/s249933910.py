m,d = map(int,input().split())
t_cnt = 0
for mon in range(1,m+1):
  for dd in range(22,d+1):
      d1 = dd%10
      if d1<2:
          continue
      d10 = (dd - d1)//10
      if d1*d10 == mon:
        t_cnt += 1

print(t_cnt)
