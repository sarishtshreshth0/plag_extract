import sys
from math import gcd

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, X = in_nn()
    x = in_nl()
    x += [X]
    x.sort()

    diff = [0] * N
    for i in range(N):
        diff[i] = x[i + 1] - x[i]

    ans = diff[0]
    for i in range(1, N):
        ans = gcd(ans, diff[i])

    print(ans)


if __name__ == '__main__':
    main()
