N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]

ab = sorted(ab, key= lambda x: [x[0], x[1]])
cd = sorted(cd, key= lambda x: [x[0], x[1]])

kouho = []
ans = 0
temp = 0

used = [False for _ in range(N)]

for i, j in cd:
    for w, kl in enumerate(ab):
        k, l = kl
        if i < k or j < l or used[w] == True:
            continue
        else:
            kouho.append([l, w])
    if len(kouho) != 0:
        kouho = sorted(kouho, key= lambda x: x[0], reverse=True)
        ans += 1
        used[kouho[0][1]] = True
        kouho = []

print(ans)