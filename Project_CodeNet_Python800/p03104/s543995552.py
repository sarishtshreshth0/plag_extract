a, b = map(int, input().split())
b = b + 1
d = 1
res = 0
t1 = a % 4
t2 = b % 4
ls = [0, 1, 0, 1]
res += (sum(ls[:t2]) - sum(ls[:t1])) % 2
while 2 ** d < max(a, b):
    tmp1 = a % (2 ** (d + 1))
    tmp2 = b % (2 ** (d + 1))
    tmp3 = max(tmp1, tmp2)
    tmp4 = min(tmp1, tmp2)
    if tmp3 >= 2 ** d:
        tmp3 = tmp3 % 2
    else:
        tmp3 = 0
    if tmp4 >= 2 ** d:
        tmp4 = tmp4 % 2
    else:
        tmp4 = 0
    tmp = (tmp4 - tmp3) % 2
    res += tmp * (2 ** d)
    d += 1

print(res)