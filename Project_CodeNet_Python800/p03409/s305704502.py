from operator import itemgetter

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dp_ab = [False] * n
dp_cd = [False] * n

ab.sort(key = itemgetter(1), reverse = True)
cd.sort()

for i in range(n):
    for j in range(n):
        if cd[i][0] > ab[j][0] and cd[i][1] > ab[j][1] and dp_cd[i] == False and dp_ab[j] == False:
            dp_cd[i] = True
            dp_ab[j] = True
            ans += 1

print(ans)
