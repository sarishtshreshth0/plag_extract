d = dict()

n = int(input())
a = [int(x) for x in input().split()]

for x in a:
  d[x - 1] = d.setdefault(x - 1, 0) + 1
  d[x] = d.setdefault(x, 0) + 1
  d[x + 1] = d.setdefault(x + 1, 0) + 1

print(sorted(d.items(), key=lambda x : x[1],  reverse=True)[0][1])