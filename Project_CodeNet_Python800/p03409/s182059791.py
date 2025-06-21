n = int(input())
ab = []
cd = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    ab.append(tmp)
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    cd.append(tmp)

AB = sorted(ab, key=lambda x: x[1],reverse=True)
CD = sorted(cd, key=lambda x: x[0])

ans = 0
for b in CD:
    for r in AB:
        if r[0] < b[0] and r[1] < b[1]:
            ans += 1
            AB.remove(r)
            break

print(ans)