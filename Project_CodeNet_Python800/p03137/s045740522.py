import math
import sys
import collections
import bisect


def main():
    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    if m <= n:
        print(0)
        return
    y = sorted([x[i + 1] - x[i] for i in range(m - 1)])
    print(sum(y[0:(m-n)]))


if __name__ == '__main__':
    main()
