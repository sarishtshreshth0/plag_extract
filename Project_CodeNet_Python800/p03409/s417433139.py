#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    R = [list(map(int,input().split())) for i in range(N)]
    B = [list(map(int,input().split())) for i in range(N)]
    R.sort(key=lambda x:x[1])
    R.sort()
    B.sort(key=lambda x:x[1])
    B.sort()
    ret = 0
    for b in B:
        pairfg = False
        pair = [1000, -1000]
        for r in R:
            if r[0] < b[0] and r[1] < b[1]:
                if r[1]>pair[1]:
                    pairfg = True
                    pair = r
        if pairfg:
            ret += 1
#            print(pair,b)
            R.remove(pair)
    print(ret)

if __name__ == '__main__':
    main()