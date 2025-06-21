N = int(input())
red = list()
blue = list()
for i in range(N):
  red.append(list(map(int, input().split())))
for i in range(N):
  blue.append(list(map(int, input().split())))
blue.sort()
redflag = [0] * N
for i in range(N):
  [c, d] = blue[i]
  tmp = -1
  maxay = -1
  for j in range(N):
    [a, b] = red[j]
    if(c > a and d > b and redflag[j] == 0 and maxay < b):
      tmp = j
      maxay = b
  if(tmp >= 0):
    redflag[tmp] = 1
print(sum(redflag))