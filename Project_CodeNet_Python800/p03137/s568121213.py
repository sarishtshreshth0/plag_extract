import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()
    Y = [0] * (M - 1)
    for i in range(M - 1):
        Y[i] = X[i + 1] - X[i]
    Y.sort(reverse=True)

    ans = sum(Y[N - 1:])
    print(ans)


if __name__ == "__main__":
    main()
