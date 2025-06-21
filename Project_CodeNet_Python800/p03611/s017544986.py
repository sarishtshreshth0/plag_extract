N = int(input())
A = list(map(int, input().split()))
d = {}
for a in A:
  for i in range(a - 1, a + 2):
    d[i] = d.get(i, 0) + 1
x = sorted(d.values())
print(max(x))