def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
aaa = list(map(int, input().split()))
cnt_l = [0] * (n - 1)
cnt_r = [0] * (n - 1)

cnt_l[0] = aaa[0]
for i in range(1, n - 1):
    cnt_l[i] = gcd(cnt_l[i - 1], aaa[i])

aaa.reverse()
cnt_r[0] = aaa[0]
for i in range(1, n - 1):
    cnt_r[i] = gcd(cnt_r[i - 1], aaa[i])

cnt_l = [cnt_r[-1]] + cnt_l
cnt_r = [cnt_l[-1]] + cnt_r
cnt_r.reverse()

ans = 1
for i in range(n):
    tmp = gcd(cnt_l[i], cnt_r[i])
    ans = max(ans, tmp)

print(ans)