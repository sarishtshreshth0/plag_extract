import sys

input = sys.stdin.readline


def main():
    M, D = map(int, input().split())

    ans = 0
    for m in range(1, M + 1):
        for d in range(10, D + 1):
            d_10 = d // 10
            d_1 = d % 10
            if d_1 >= 2 and d_10 >= 2 and d_1 * d_10 == m:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
