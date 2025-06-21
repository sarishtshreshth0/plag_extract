M, D = map(int, input().split())
ans = 0
for i in range(1,M+1):
  for j in range(2,10):
    if i % j == 0 and 2 <= i//j < 10:
      if 10*j + i//j <= D:
        # print(i,j,i//j)
        ans += 1
print(ans)