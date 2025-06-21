from collections import deque
n = int(input())

r=[]
b=[]
for i in range(n):
  r.append(list(map(int, input().split())))
for i in range(n):
  b.append(list(map(int, input().split())))
r.sort(key=lambda x: x[1], reverse=True)
b.sort()
for bi in b:
  for i in range(len(r)):
    if r[i][0] < bi[0] and r[i][1] < bi[1]:
      r = r[:i] + r[i+1:]
      break
print(n - len(r))