import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N, M = in_nn()
    X = sorted(in_nl())

    X_diff = [0] * (M - 1)
    for i in range(M - 1):
        X_diff[i] = X[i + 1] - X[i]

    X_diff.sort(reverse=True)
    # print(X_diff)
    # print(X)
    N = min(N, M)
    ans = X[-1] - X[0] - sum(X_diff[:N - 1])
    print(ans)


if __name__ == '__main__':
    main()
