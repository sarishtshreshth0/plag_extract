def main():
    n = int(input())
    d = list(map(int,input().split()))
    mod = 998244353
    if d[0]!=0:
        print(0)
        return
    D = {0:1}
    for i in range(1,n):
        if d[i]==0:
            print(0)
            return
        if D.get(d[i]) == None:
            D[d[i]] = 1
        else:
            D[d[i]] += 1
    ans = 1
    if sorted(D.keys())[-1]!=len(D.keys())-1:
        print(0)
        return
    for k in range(1,len(D.keys())):
        ans *= pow(D[k-1],D[k],mod)
        ans = ans % mod
    print(ans)

if __name__ == "__main__":
    main()
