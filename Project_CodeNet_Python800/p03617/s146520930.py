#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def main():
    P = list(map(int, input().split()))
    N = int(input())
    p = min(P[0]*4, P[1]*2, P[2])
    print(min(N*p, (N//2)*P[3] + (N%2)*p))

if __name__ == '__main__':
    main()