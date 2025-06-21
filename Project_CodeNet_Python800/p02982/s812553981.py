n, d = map(int,input().split())
points = []

for i in range(n):
  points.append(list(map(int,input().split())))

def distance(a, b):
  dist = 0
  
  for a, b in zip(a, b):
    dist += (a - b) ** 2

  if dist == 0:
    return False
  return int(dist ** 0.5) ** 2 == dist

count = 0

for pa in points:
  for pb in points:
    if distance(pa, pb):
      count += 1

print(count // 2)