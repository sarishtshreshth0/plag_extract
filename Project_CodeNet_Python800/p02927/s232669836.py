def d10(n):
    return n//10
def d1(n):
    return n%10
def sekinohi(m, d):
    return d1(d)>=2 and d10(d)>=2 and m==d1(d)*d10(d)

ans = 0
m, d = map(int, input().split())
for i in range(1, m+1):
    for j in range(1, d+1):
        if sekinohi(i, j):
            ans += 1
print(ans)