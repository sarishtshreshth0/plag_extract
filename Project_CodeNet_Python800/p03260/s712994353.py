a,b = map(int, input().split())
ans = 0
for i in range(1, 4):
  if a*b*i%2 == 1:
    ans += 1
    
if ans > 0:
  print("Yes")
else:
  print("No")