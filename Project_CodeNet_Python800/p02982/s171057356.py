import sys
from math import sqrt


def dist(x, d, i, j):
    res = 0
    for k in range(d):
        res += (x[i][k] - x[j][k]) ** 2
    return res


def main():
    input = sys.stdin.buffer.readline
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sqrt(dist(x, d, i, j)).is_integer():
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
