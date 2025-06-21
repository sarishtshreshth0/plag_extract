M, D = map(int, input().split())

ret = 0
for d1 in range(2, 10) :
    for d10 in range(2, 10) :
        if d10 * 10 + d1 <= D and d10 * d1 <= M :
            ret += 1
print(ret)