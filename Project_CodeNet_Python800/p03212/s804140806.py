n = int(input())
keta = len(str(n))

if keta <= 2:
    print(0)
else:
    # keta-1までのパターン
    ans = 0
    # for k in range(3, keta):
    #    ans = pow(3, k) - 3 - (3*(pow(2, k) + 2))

    from itertools import product
    for k in range(3, keta+1):
        for l in product(['3', '5', '7'], repeat=k):
            if not '3' in l or not '5' in l or not '7' in l:
                continue
            nn = int(''.join(l))
            if nn <= n:
                ans += 1

    print(ans)
