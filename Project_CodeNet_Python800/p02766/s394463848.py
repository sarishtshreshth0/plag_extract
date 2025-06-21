N, K = map(int ,input().split())
counter = 0
while N:
  N //= K
  counter += 1
print(counter)