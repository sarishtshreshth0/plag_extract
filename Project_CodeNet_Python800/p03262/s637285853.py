N, X = map(int, input().split())
x_list = list(map(int, input().split()))

import numpy as np
import fractions

a = list(set(abs(np.array(x_list) - X)))
ans = a[0]
for i in range(1, len(a)):
    ans = fractions.gcd(ans, a[i])
print(ans)