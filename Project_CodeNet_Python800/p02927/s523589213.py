M, D = map(int, input().split())
ans = 0

for m in range(1, M+1):
  for d in range(11, D+1):
    d = str(d)
    d10 = int(d[0])
    d1 = int(d[1])
    
    if d1 >= 2 and d10 >= 2 and m == d1 * d10:
      ans += 1
    
print(ans)