p = list(map(int, input().split()))
n = int(input())
eff = [p[0], p[1] / 2, p[2] / 4, p[3] / 8]
g = [0.25, 0.5, 1, 2]
total = 0
ans = 0
def calc(i):
    global total, ans
    k = eff.index(min(eff[: i + 1]))
    ans += int((n - total) // g[k] * p[k])
    total += (n - total) // g[k] * g[k]


while total != n:
    if n - total >= 2:
        calc(3)
    elif n - total >= 1:
        calc(2)
    elif n - total >= 0.5:
        calc(1)
    else:
        total += 0.25
        ans += p[0]
print(ans)