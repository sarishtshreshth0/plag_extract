import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    d = list(map(int,input().split()))
    if d[0] != 0:
        print(0)
    else:
        MOD = 998244353
        use = [0 for _ in range(max(d)+1)]
        for num in d:
            use[num] += 1
        if use[0] != 1:
            print(0)
        else:
            ans,pa = 1,1
            for num in use:
                ans *= pow(pa,num,MOD)
                ans %= MOD
                pa = num
            print(ans)

if __name__ == "__main__":
    main()
