
M, D = [int(x) for x in raw_input().split(' ')]
res = 0
for i in xrange(2, 10):
    for j in xrange(2, 10):
        if i * j <= M and i * 10 + j <= D:
            res += 1
print(res)
