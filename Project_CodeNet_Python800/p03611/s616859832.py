N = int(input())
l = [0]*100003
for a in map(int, input().split()):
  l[a+1] += 1
  l[a] += 1
  if a-1 < 0:
    continue
  else:
    l[a-1] += 1

print(max(l))