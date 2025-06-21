import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    m, d = list(map(int, readline().split()))
    cnt = 0
    for i in range(1, m + 1):
        for j in range(22, d + 1):
            t = 1
            for v in str(j):
                t *= int(v) if int(v) >= 2 else -1
            if i == t:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
