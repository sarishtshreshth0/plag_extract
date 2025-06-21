import sys

N, K = map(int, sys.stdin.buffer.read().split())

i = 0
while N:
  N //= K
  i += 1

print(i)
