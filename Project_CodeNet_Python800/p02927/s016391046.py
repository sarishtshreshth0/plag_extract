M, D = map(int, input().split())
def judge(m, d):
    if len(d) == 2 and m == int(d[0]) * int(d[1]) and int(d[0]) >= 2 and int(d[1]) >= 2:
        return 1
    else:
        return 0
ans = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        ans += judge(m, str(d))
print(ans)