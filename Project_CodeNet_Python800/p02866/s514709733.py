import collections
MOD = 998244353
def main():
    N = int(input())
    D = [int(_) for _ in input().split()]
    Dmax = max(D)
    cc = collections.Counter(D)
    if D[0] != 0: return 0
    if cc[0] != 1: return 0
    for i in range(Dmax+1):
        if cc[i] == 0: return 0
    output = 1
    for i in sorted(cc.keys()):
        if i in (0, 1): continue
        output *= pow(cc[i-1], cc[i], MOD)
        output %= MOD
    return output

if __name__ == '__main__':
    print(main())
