n, d = map(int, input().split())
x = list(list(map(int, input().split())) for _ in range(n))

cnt = 0
for i in range(n - 1):
  
  for j in range(i + 1, n):
    sq_dis = 0
    
    for k in range(d):
      sq_dis += (x[i][k] - x[j][k])**2
      
    dis = sq_dis ** 0.5

    if dis.is_integer() == True:
      cnt += 1
        
print(cnt)