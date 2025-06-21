import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    D = in_nl()
    mod = 998244353

    if D[0] != 0:
        print(0)
        exit()

    for i in range(1, N):
        if D[i] == 0:
            print(0)
            exit()

    count = [0] * N
    for i in range(N):
        count[D[i]] += 1

    zero = N + 1
    non_zero = -1
    for i in range(N):
        if count[i] == 0:
            zero = min(zero, i)
        else:
            non_zero = max(non_zero, i)

    if zero < non_zero:
        print(0)
        exit()

    ans = 1
    for i in range(1, N):
        if count[i] == 0:
            break
        else:
            ans *= count[i - 1] ** count[i]
            ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
