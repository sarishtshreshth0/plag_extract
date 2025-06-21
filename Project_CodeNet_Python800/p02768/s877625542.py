N, a, b = map(int, input().split())
modz = 10**9 + 7

def repeatSquaring(N, P, M):
    if P <= 0:
        return 1
    if (P &0x01) == 0:
        ans = repeatSquaring(N, (P>>1), M)
        return ans*ans % M

    return N*repeatSquaring(N, P-1, M) % M

def seki(aa, bb):
    res = 1
    for k in range(aa, bb+1):
        res *= k
        if res >= modz:
            res %= modz
    return res

def CC(aa, nn):
    ss = repeatSquaring(seki(1, aa), modz - 2, modz)
    return seki(nn-aa + 1, nn)*ss % modz

total = repeatSquaring(2, N, modz) - 1
total -= CC(a, N)
if total < 0: total += modz

total -= CC(b, N)
if total < 0: total += modz

print(int(total))