N, K = map(int, input().split())
l = []
while N // K != 0:
  l.insert(-1, N % K)
  N = N // K
l.append(N)
print(len(l))