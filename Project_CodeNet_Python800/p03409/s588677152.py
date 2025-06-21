n = int(input())
red = []
blue = []
B = [0]*(n+1)
for i in range(n):
  red.append(list(map(int,input().split())))

for i in range(n):
  blue.append(list(map(int,input().split())))
red.sort(key=lambda x: x[1], reverse=True)
blue.sort(key=lambda x: x[0])
cnt = 0

for i in range(n):
  for j in range(n):
    if (red[j][0] < blue[i][0] and red[j][1] < blue[i][1]) and B[j+1] == 0:
      B[j+1] = 1
      cnt += 1
      break

print(cnt)