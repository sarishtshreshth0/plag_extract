from collections import Counter

if __name__ == '__main__':
    MOD = 998244353
    n = int(input())
    d = list(map(int, input().split()))
    if d[0] != 0:
        print(0)
        exit(0)
    c = Counter(d)
    if c[0] != 1:
        print(0)
        exit(0)
    ans = 1
    for i in range(n - 1):
        ans *= pow(c[i], c[i + 1], MOD)
        ans %= MOD
    print(ans)
