import sys
import itertools
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    A = in_nl()

    asum = list(itertools.accumulate([0] + A))
    count = Counter(asum)

    ans = 0
    for k, v in count.items():
        ans += v * (v - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
