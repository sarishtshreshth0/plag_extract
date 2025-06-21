n = int(input())
csf = [list(map(int, input().split())) for i in range(n - 1)]
for i in range(n):
    ans = 0
    for j in range(i, n - 1):
        c, s, f = csf[j][0], csf[j][1], csf[j][2]
        if ans < s:
            ans = s
        elif ans % f != 0:
            ans += f - ans % f
        ans += c
    print(ans)