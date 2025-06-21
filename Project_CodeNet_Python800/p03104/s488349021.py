import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def f(n):
    if n % 2 == 0:
        a = n // 2
        if a % 2 == 0:
            return n
        else:
            return n ^ 1
    else:
        a = n // 2
        if a % 2 == 0:
            return 1
        else:
            return 0


def main():
    A, B = map(int, input().split())
    a = f(A - 1)
    b = f(B)
    answer = a ^ b

    print(answer)


if __name__ == "__main__":
    main()
