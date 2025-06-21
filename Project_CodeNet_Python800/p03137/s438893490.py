import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if M <= N:
        print(0)
        exit()

    diff = [0] * (M - 1)
    for i in range(M - 1):
        diff[i] = X[i + 1] - X[i]

    diff.sort()
    print(sum(diff[:M-N]))


if __name__ == "__main__":
    main()
