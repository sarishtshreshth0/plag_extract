import itertools
N = int(input())
A = ["3", "5", "7"]
L = []
for i in range(1, 10):
  for l in itertools.product(A, repeat=i):
    L.append(l)
c = 0
for l in L:
  if int("".join(l))<=N and l.count("3")>=1 and \
  l.count("5")>=1 and l.count("7")>=1:
    c += 1
print(c)