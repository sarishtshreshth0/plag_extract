#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit(0)
if n == 2:
    if abs(a[0]-a[1]) <= 2:
        print(2)
    else:
        print(1)
    exit(0)

if n >= 3:
    d = [0 for _ in range(100001)]
    for i in range(n):
        d[a[i]] += 1
    ans = 0 
    for i in range(100001-2):
        tmp = d[i] + d[i+1] + d[i+2]
        if ans <= tmp:
            ans = tmp 

print(ans)
