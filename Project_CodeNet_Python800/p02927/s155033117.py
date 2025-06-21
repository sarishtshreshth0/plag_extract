import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    M, D = map(int, readline().split())
    ans = 0
    for m in range(1, M + 1):
        for d in range(10, D + 1):
            d_str = str(d)
            d_1 = int(d_str[1])
            d_10 = int(d_str[0])
            if d_1 >= 2 and d_10 >= 2:
                if d_1 * d_10 == m:
                    ans += 1

    print(ans)

if __name__ == '__main__':
    main()
