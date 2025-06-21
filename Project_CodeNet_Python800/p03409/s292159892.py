n = int(input())
R = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
R.sort()
B.sort()
pair = []

for bx, by in B:
    tmp = [r for r in R if r[0] < bx]
    tmp.sort(key=lambda x: x[1])
    for rx, ry in tmp[::-1]:
        if ry < by:
            pair.append([[rx, ry], [bx, by]])
            R.pop(R.index([rx, ry]))
            break

print(len(pair))