s = list(map(int, input().split()))
n = int(input()) * 100
ss = [s[0] * 4, s[1] * 2, s[2], s[3] // 2]
ll = [25, 50, 100, 200]
cost = 0
while n > 0:
    if n >= 200:
        pass
    elif n >= 100:
        ss = ss[:3]
        ll = ll[:3]
    elif n >= 50:
        ss = ss[:2]
        ll = ll[:2]
    else:
        ss = ss[:1]
        ll = ll[:1]
    ssm = ss.index(min(ss))
    cnt = n // ll[ssm]
    cost += s[ssm] * cnt
    n -= ll[ssm] * cnt
print(cost)