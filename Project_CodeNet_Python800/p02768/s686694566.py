n, a, b = list(map(int, input().split(' ')))

# 二項係数 mod [検索]
mmm = 1000000000 + 7
fac = []
inv = []
inv_fac = []
def init(n):
    fac.append(1)
    fac.append(1)
    inv.append(0)
    inv.append(1)
    inv_fac.append(1)
    inv_fac.append(1)
    for i in range(2, n):
        fac.append(fac[-1] * i % mmm)
        inv.append(mmm - inv[mmm%i] * (mmm // i) % mmm)
        inv_fac.append(inv_fac[-1] * inv[-1] % mmm)

def choice(a, b):
    if a < b:
        return 0
    v = 1
    for i in range(b):
        v = (v * (a-i)) % mmm  # 偶然通っていたけどここはnではなくa (eの途中で気づいた)
    return v * inv_fac[b]

init(int(2e5) + 1)


ans = pow(2, n, mmm) - 1  # v, e, mod
bunshi = 1
for i in range(a):
    bunshi = (bunshi * (n-i)) % mmm
ans -= choice(n, a)
ans -= choice(n, b)
print(ans % mmm)

'''
4, 1, 3 => 4c2 + 4c4 -> 6+1 = 7
4 + 6 + 4 + 1 - 4c1 - 4c2 
1        1
11       2
121      4
1331     8
14641   16, 0が無いので-1, 大きい combination -> 二項係数 mod [検索]
'''
