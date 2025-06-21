#!/usr/bin/env python3


def main():
    N, K = map(int, open(0).read().split())
    i = 0
    while N != 0:
        N = N // K
        i += 1
    print(i)


main()
