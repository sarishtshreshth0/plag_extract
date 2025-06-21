def main():
    n = int(input())
    d = list(map(int,input().split()))
    md = 998244353

    if d[0] != 0:
        print(0)
        return 0

    dp = [0]*n
    for i in d:
        dp[i]+=1
    res = 1
    for i in d[1:]:
        res = (res * dp[i-1]) % md
    print(res%md)

if __name__ == '__main__':
    main()
