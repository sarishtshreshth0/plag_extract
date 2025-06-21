m,d = map(int,input().split())
ans = 0
for i in range(1,d+1):
  if i < 22:
    continue
  else:
    if i%10 == 0:
      continue
    else:
      if i%10 == 0 or i%10 == 1:
        continue
      else:
        if (i//10)*(i%10) <= m:
          ans += 1
print(ans)