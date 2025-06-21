import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    m, d = map(int, readline().rstrip().split())
    if d < 10:
        print(0)
        return

    cnt = 0
    for k in range(1, m + 1):
        for i in range(10, d + 1):
            d1, d10 = int(str(i)[1]), int(str(i)[0])
            if d1 * d10 == k and d1 > 1 and d10 > 1:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
