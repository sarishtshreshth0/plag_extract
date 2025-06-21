import math
N, K = [int(i) for i in input().split()]
print(math.floor(math.log(N, K)) + 1)