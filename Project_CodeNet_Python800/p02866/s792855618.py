#!/usr/bin/env python3

from collections import Counter

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

MOD = 998244353

def main():
    N = II()
    D = LII()

    if D[0] != 0 or D.count(0) > 1:
       print(0)
       return 
    
    c = Counter(D)
    res = 1

    if c[0] > 1:
       print(0)
       return
    
    mx = max(c.keys())
    for i in range(1, mx+1):
        if i not in c:
            print(0)
            return
        
        res = (res * c[i-1] ** c[i]) % MOD

    print(res)

if __name__ == '__main__':
    main()
