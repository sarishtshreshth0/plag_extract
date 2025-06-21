#!/usr/bin/env python3

N = int(input())
data = []
for _ in range(N - 1):
    data.append(tuple(map(int, input().split())))

for i in range(N - 1):
    c_i, s_i, f_i = data[i] 
    ans = c_i + s_i
    if i == N - 2:
        print(ans)
        continue
    for j in range(i + 1, N - 1):
        c_j, s_j, f_j = data[j]
        if ans >= s_j:
            tmp = (ans - s_j) % f_j
            ans += c_j if tmp == 0 else f_j - tmp + c_j
        else:
            ans += s_j - ans + c_j
    print(ans)

print(0)