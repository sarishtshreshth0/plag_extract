import sys

input = sys.stdin.readline


def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())

    ans = 0
    price_of_1_L = min(4 * Q, 2 * H, S)
    if D < 2 * price_of_1_L:
        n_D = N // 2
        ans += D * n_D
        N -= 2 * n_D
    ans += N * price_of_1_L

    print(ans)


if __name__ == "__main__":
    main()
