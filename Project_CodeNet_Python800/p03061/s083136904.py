import sys
from fractions import gcd


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [A[0]]
    right = [A[-1]]
    for i in range(1, N - 1):
        left.append(gcd(left[-1], A[i]))
        right.append(gcd(right[-1], A[N - i - 1]))
    answer = max(left[-1], right[-1])
    for i in range(N - 2):
        g = gcd(left[i], right[N - 3 - i])
        if answer < g:
            answer = g
    print(answer)


if __name__ == "__main__":
    main()
