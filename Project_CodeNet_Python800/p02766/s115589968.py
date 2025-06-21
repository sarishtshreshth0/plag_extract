import math
n, k = map(int, input().split())
print(int(math.floor(math.log(n, k) + 1)))