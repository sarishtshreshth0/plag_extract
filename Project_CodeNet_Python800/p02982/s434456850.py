n,d=map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
squares=[i*i for i in range(200)]
cnt=0
for i in range(n):
  for j in range(i+1,n):
    distance=0
    for k in range(d):
      distance+=(a[i][k]-a[j][k])**2
    if distance in squares:
      cnt+=1
print(cnt)