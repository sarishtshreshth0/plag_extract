#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1,N):
        A[i]+=A[i-1]
    A = Counter(A)
    ret = 0
    for x in A.values():
        ret += x*(x-1)//2
    ret += A.get(0,0)
    print(ret)

if __name__ == '__main__':
    main()