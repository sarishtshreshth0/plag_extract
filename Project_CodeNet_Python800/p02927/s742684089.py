import sys
m, d = map(int, input().split())

if d < 22 or m < 4:
    print(0)
    sys.exit()

ans = 0
for i in range(4, m+1):
    for j in range(22, d+1):
        d_0 = j % 10
        d_10 = j // 10
        if d_0 == 1 or d_10 == 1:
            continue
        if d_0 * d_10 == i:
            ans += 1

print(ans)