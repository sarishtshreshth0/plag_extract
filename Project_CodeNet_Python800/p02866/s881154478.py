#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    N = int(input())
    D = list(map(int, input().split()))
    Dc = Counter(D)

    if D[0]!=0 or Dc[0]!=1:
        print(0)
    else:
        mx = max(D)
        mod = 998244353
        ret = 1
        for i in range(1, mx+1):
            ret *= pow(Dc.get(i-1,0), Dc.get(i,0), mod)
            ret %= mod
        print(ret)

if __name__ == '__main__':
    main()