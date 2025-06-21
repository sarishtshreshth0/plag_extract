#!/usr/bin/env python3
# 整数の入力
N = int(input())
data = [list(map(int, input().split())) for _ in range(N-1)]
# print(N)
#print(data)


for i in range(N-1):
    t = 0
    for j in range(i, N-1):
        #print(j)
        c = data[j][0]
        s = data[j][1]
        f = data[j][2]
        if t < s: 
            t = s
        elif t % f == 0:
            pass
        else:
            t += f - (t%f)
        t += c
    print(t)
        

print(0)