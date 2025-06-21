N = int(input())

import math
a = math.floor(math.sqrt(N))
amax = 1
for i in range(1, a+1):
    if N % i == 0:
        amax = i

print(math.floor(math.log10(N//amax)) + 1)