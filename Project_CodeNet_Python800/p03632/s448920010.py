a, b, c, d = map(int, input().split())

area = [0 for i in range(max([b,d])+1)]

for i in range(a,b):
  area[i] += 1;

for i in range(c,d):
  area[i] += 1;

answer = 0
for i in area:
  if i == 2:
    answer += 1

print(answer)