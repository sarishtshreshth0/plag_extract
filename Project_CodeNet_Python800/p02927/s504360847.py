M, D = map(int, input().split())

ans = 0

if D < 22:
    print(0)
    exit()

for m in range(1, M+1):
    for d in range(22, D+1):
        d1, d10 = d%10, d//10
        ans += (d1 >= 2 and d10 >= 2 and d1 * d10 == m)

print(ans)
