#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
arr = [0] * 100002

for i in range(n):
    arr[a[i] + 1] += 1
    arr[a[i]] += 1
    arr[a[i] + 2] += 1

print(max(arr))
