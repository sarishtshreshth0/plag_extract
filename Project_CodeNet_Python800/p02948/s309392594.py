# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:06:07 2020

@author: Kanaru Sato
"""

import heapq

n,m = list(map(int, input().split()))
albeit = []
for i in range(m+1):
    albeit.append([])

for i in range(n):
    a,b = list(map(int, input().split()))
    if a <= m:
        albeit[a].append(-1*b)

##print(albeit)
Heap = [0]
sum = 0
for i in range(m):
    day = i+1
    for money in albeit[day]:
        heapq.heappush(Heap, money)
    if Heap[0] != 0:
        daymax = heapq.heappop(Heap)*-1
        sum += daymax

print(sum)