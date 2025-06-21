m, d = map(int, input().split())

cnt = 0
if m < 4 or d < 22:
  pass
else:
  for i in range(22, d+1):
    if (i // 10) >= 2 and (i % 10) >= 2:
      if (i // 10) * (i % 10) <= m:
        cnt += 1
        
        
print(cnt)