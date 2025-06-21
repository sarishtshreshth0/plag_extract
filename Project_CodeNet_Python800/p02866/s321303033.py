def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input()) 
    d = list(map(int, input().split()))
    mod = 998244353
    from collections import Counter as cc
    c = cc(d)
    if c[0] != 1 or d[0] != 0:
        print(0)
        return
    m = max(d)
    ans = 1
    for i in range(1, m+1):
        ans *= pow(c[i-1], c[i], mod)
        ans %= mod
    print(ans)
    
    
if __name__ == '__main__':
    main()