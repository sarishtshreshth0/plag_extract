import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C = list(map(int, sys.stdin.buffer.readline().split()))

    print('Yes' if A <= C and C <= B or A >= C and C >= B else 'No')


if __name__ == '__main__':
    main()
