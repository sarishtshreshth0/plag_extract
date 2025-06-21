#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    S = input()
    nw = S[0]
    ret = 1
    for i in range(1,N):
        if nw == S[i]:
            continue
        else:
            nw = S[i]
            ret += 1
    print(ret)

if __name__ == '__main__':
    main()