# -*- coding: utf-8 -*-
import numpy as np
n = int(input())

cum = np.array(list(map(int, input().split()))).cumsum()
ans = cum[-1]
for i in range(n-1):
    ans = min(ans, abs(2*cum[i]-cum[-1]))
print(ans)
