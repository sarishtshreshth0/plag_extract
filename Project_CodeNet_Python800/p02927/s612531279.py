M, D = input().split()
M = int(M)
d10 = int(D[0])
if len(D) >1:
  d1 = int(D[1])
ans = 0
for i in range(2,d10+1):
  for j in range(2,10):
    if i == d10 and j<=d1 and i*j <= M:
      ans += 1
     
    elif i*j <= M and i<d10:
      ans += 1
      
print(ans)
