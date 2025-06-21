def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    def nc2(n):
        return n*(n-1)//2

    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])
    from collections import Counter as cc
    c = cc(s)
    ans = 0
    for x in c:
        if c[x] > 1:
            ans += nc2(c[x])
    print(ans)



    
if __name__ == '__main__':
    main()