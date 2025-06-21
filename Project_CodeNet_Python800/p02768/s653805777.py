def main():
    n,a,b = map(int,input().split())
    mod = 10**9+7
    s = pow(2,n,mod)
    nCa,nCb = 1,1
    for i in range(n-a+1, n+1):
        nCa *= i
        nCa %= mod

    for i in range(1,a+1):
        nCa *= pow(i,mod-2,mod)
        nCa %= mod

    for i in range(n-b+1, n+1):
        nCb *= i
        nCb %= mod

    for i in range(1,b+1):
        nCb *= pow(i,mod-2,mod)
        nCb %= mod
    print((s-nCa-nCb-1)%mod)


if __name__ == "__main__":
    main()
