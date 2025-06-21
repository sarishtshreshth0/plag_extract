#coding: utf-8
import math
N = int(input())
L = []
for i in range(N-1):
    l = list(map(int,input().split()))
    L.append(l)

for i in range(N-1):
    t = 0
    for j in range(i,N-1):
        l = L[j]
        c = l[0]
        s = l[1]
        f = l[2]
        if t <= s:
            t = s+c
        else:
            n = math.ceil((t-s)/f)
            t = s+n*f+c
    print(t)

print(0)