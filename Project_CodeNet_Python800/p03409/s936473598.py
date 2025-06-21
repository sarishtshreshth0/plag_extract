import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())

    red = [list(map(int, readline().split())) for _ in range(n)]
    blue = [list(map(int, readline().split())) for _ in range(n)]

    from operator import itemgetter

    red.sort()
    blue.sort()

    ans = 0

    for bx, by in blue:
        ry_max = -1
        r_idx = -1

        for ri, ele in enumerate(red):
            rx = ele[0]
            ry = ele[1]
            if rx < bx and ry < by:
                if ry > ry_max:
                    ry_max = ry
                    r_idx = ri

        if r_idx != -1:
            del red[r_idx]
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
