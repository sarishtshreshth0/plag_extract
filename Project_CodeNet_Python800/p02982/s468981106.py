import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def distance2_nd(p, q):
    return sum((px - qx) ** 2 for px, qx in zip(p, q))


def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1) // 2
        y = (x + n // x) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    elif n == 0:
        return 0
    else:
        raise ValueError("isqrt() argument must be nonnegative")


def main():
    N, D = map(int, readline().split())
    X = [list(map(int, readline().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            d2 = distance2_nd(X[i], X[j])
            di = isqrt(d2)
            if di * di == d2:
                ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
