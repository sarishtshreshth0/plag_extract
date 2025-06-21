# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


mod = 10 ** 9 + 7
N, M = list(map(int, input().split()))
A = [0]*N
B = [0]*N
# 日数別にもらえる額を管理
# money = defaultdict(list)
keys = list(range(1, 1+10**5))
# print(keys)
values = [[] for i in range(1, 1+10**5)]
job = dict(zip(keys, values))
for i in range(N):
    a, b = map(int, input().split())
    job[a].append(-b)
    # A[i], B[i] = a, b
# A日後にB円もらえる、M日後に報酬最大化
ans = 0
can_work = []
heapq.heapify(can_work)
for delay in range(1, 1+M):
    for item in job[delay]:
        heapq.heappush(can_work, item)
    # print('delay', delay)
    # print(job)
    if (len(can_work) != 0):
        ans -= heapq.heappop(can_work)

    # for i in range(delay):
    #     print(delay-i)
    #     if len(jpb[delay-i]) != 0:
    #         print('found')
    #         max_money = max(jpb[delay-i])
    #         ans += max_money
    #         jpb[delay-i].remove(max_money)
    #         jpb[delay-i]
    #         break
    #     print('===========')
print(ans)
