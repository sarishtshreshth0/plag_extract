import bisect

N = int(input())
Red = [tuple(map(int, input().split())) for _ in range(N)]
Blue = [tuple(map(int, input().split())) for _ in range(N)]
Done = [False] * N
Red.sort()
Blue.sort()
Redx = []
Redy = []
ans = 0
for x, y in Red:
    Redx.append(x)
    Redy.append(y)

for x, y in Blue:
    i = bisect.bisect_left(Redx, x)
    m = -1
    num = -1
    for j in range(i):
        if Redy[j] >= y or Done[j]:
            continue
        if Redy[j] > m:
            m = Redy[j]
            num = j
    if num != -1:
        ans += 1
        Done[num] = True
print(ans)


