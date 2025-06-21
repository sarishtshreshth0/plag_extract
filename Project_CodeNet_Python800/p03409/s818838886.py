N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]
dic = {}
for a, b in ab:
    dic[(a, b)] = 0
for c, d in cd:
    dic[(c, d)] = 0

ab = sorted(ab, key=lambda x: (-x[0], -x[1]))
cd = sorted(cd, key=lambda x: (x[1], x[0]))

ans = 0
for c, d in cd:
    for a, b in ab:
        if a < c and b < d and dic[(a, b)] == 0 and dic[(c, d)] == 0:
            ans += 1
            dic[(a, b)] += 1
            dic[(c, d)] += 1
print(ans)