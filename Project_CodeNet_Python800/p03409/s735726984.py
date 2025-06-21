n = int(input())
red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]

red.sort(key=lambda x:x[1], reverse=True)
blue.sort()
chk = [False] * n

for b in blue:
    for i, r in enumerate(red):
        if chk[i]:
            continue
        elif r[0] < b[0] and r[1] < b[1]:
            chk[i] = True
            break
print(sum(chk))

