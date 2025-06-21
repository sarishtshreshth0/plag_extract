n = int(input())

r = [[0,0,1] for i in range(n)]
for i in range(n) :
  x,y = map(int,input().split())
  r[i][0],r[i][1] = x,y
  
b = [[0,0,1] for i in range(n)]
for i in range(n) :
  x,y = map(int,input().split())
  b[i][0],b[i][1] = x,y
  
r.sort(key=lambda x: x[0],reverse=True)
b.sort(key=lambda x: x[1])

ans = 0
for i in range(n) :
  for j in range(n) :
    if r[i][2] == 0 or b[j][2] == 0 :
      continue
    if r[i][0] < b[j][0] and r[i][1] < b[j][1] :
      r[i][2] = 0 ; b[j][2] = 0
      ans += 1
      
print(ans)