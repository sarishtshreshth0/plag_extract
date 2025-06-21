n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for i in range(n)]

b.sort(key=lambda x: x[0])
a.sort(key=lambda x: x[1])
seen = [0]*n
count = 0

for i in range(n):
  for j in range(n):
    if (seen[j] == 0) and (a[-(i+1)][0] < b[j][0]) and (a[-(i+1)][1] < b[j][1]):
      seen[j] = 1
      count = count + 1
      break
      
print(count)