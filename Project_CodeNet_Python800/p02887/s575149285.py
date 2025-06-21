#!/usr/bin/env python3

N = int(input())
S = input()

cnt = 1

check = S[0]

for i, s in enumerate(S[1:]):
    if s == check:
        if i == N - 1:
            cnt += 1
        continue
    else:
        cnt += 1
        check = s

print(cnt)
