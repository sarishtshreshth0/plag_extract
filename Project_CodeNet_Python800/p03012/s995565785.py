import sys

input = sys.stdin.readline


def main():
    N = int(input())
    W = list(map(int, input().split()))

    S1 = 0
    S2 = sum(W)
    ans = 10 ** 18
    for i in range(N - 1):
        S1 += W[i]
        S2 -= W[i]
        diff = abs(S1 - S2)
        ans = min(ans, diff)

    print(ans)


if __name__ == "__main__":
    main()
