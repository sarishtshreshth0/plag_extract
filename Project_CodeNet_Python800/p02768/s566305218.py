def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, a, b = map(int, input().split())
    mod = 10 **9 + 7
    ans = pow(2, n, mod) -1
    c = 1
    for i in range(b):
        c *= n-i
        c%= mod
        c *= pow(i+1, mod-2, mod)
        c %= mod
        if i == a-1:
            ca = c
    ans -= (c+ca)%mod
    ans %= mod
    print(ans)
    





if __name__ == '__main__':
    main()