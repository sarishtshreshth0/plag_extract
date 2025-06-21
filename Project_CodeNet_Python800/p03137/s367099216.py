#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    if n >= m:
        print(0)
    else:
        dis = []
        for i in range(m - 1):
            dis.append(x[i + 1] - x[i])
        dis.sort(reverse=True)
        print(max(x) - min(x) - sum(dis[:n - 1]))



if __name__ == '__main__':
    main()
