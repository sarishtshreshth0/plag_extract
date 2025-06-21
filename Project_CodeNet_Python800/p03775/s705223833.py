n = int(input())

import math
m = math.ceil(math.sqrt(n))

val = []
for i in range(m):
    if n % (i+1) == 0:
        val.append(len(str(n//(i+1))))
print(min(val))