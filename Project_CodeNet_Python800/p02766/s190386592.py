from math import log, ceil

N, K = map(int, input().split())
res = ceil(log(N, K))
if res == 0:
    res = 1
print(res)