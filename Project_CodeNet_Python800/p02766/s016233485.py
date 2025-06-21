from math import log, floor

N, K = map(int, input().split())

print(floor(log(N, K))+1)