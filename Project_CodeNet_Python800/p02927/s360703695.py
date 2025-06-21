m,d = map(int,input().split())
ans = 0
for i in range(1,m+1):
  for j in range(10,d+1):
    if "1" in list(str(j)):
      continue
    j1 = j//10
    j2 = j%10
    if i == j1*j2:
      ans += 1
print(ans)