M,D = map(int,input().split())
count = 0
for i in range(1,M+1):
  for j in range(1,D+1):
    if j >21:
      a = j//10
      b = j%10
      if i == int(a*b) and a>=2 and b>=2:
        
        count += 1
print(count)