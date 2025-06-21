n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]

cd.sort()
remain = set(range(n))

ans = 0
for c,d in cd:
    cand = [-1, -1]
    for i in remain:
        a,b = ab[i]
        if((a<c) & (b<d)):
            if(cand[1] < b):
                cand = [i,b]

    if(cand[0] == -1):
        continue

    remain.remove(cand[0])
    ans += 1


print(ans)