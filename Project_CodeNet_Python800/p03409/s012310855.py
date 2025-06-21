n = int(input())
ab = [ list(map(int, input().split())) for _ in range(n) ]
cd = [ list(map(int, input().split())) for _ in range(n) ]
ab = sorted(ab, key=lambda x:x[1]*(-1))
cd = sorted(cd)
ans = 0
for q in cd:
    for p in ab:
        if q[0] > p[0] and q[1] > p[1]:
            ans += 1
            ab.remove(p)
            break
print(ans)