import numpy
import math
n = int(input())
w = list(map(int, input().split()))

sum_w = sum(w)
sum_w = sum_w / 2

res = numpy.cumsum(w)

diff = [2.0 * math.fabs(res[i] - sum_w) for i in range(n)]
print(int(min(diff)))