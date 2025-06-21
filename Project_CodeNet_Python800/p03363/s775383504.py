# -*- coding: utf-8 -*-
import collections
n = int(input())
a = [int(i) for i in input().split()]

#累積和を求める
sum_a = [0 for _ in range(n+1)]
for i in range(1, n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]
#print(sum_a)

ans = 0
c = collections.Counter(sum_a)
for i in set(sum_a):
    tmp = c[i]
    if tmp >= 2:
        ans += (tmp * (tmp - 1)) // 2
print(ans)
