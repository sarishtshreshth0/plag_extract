import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, Y = list(map(int, sys.stdin.readline().split()))
    print(X + (Y//2))


if __name__ == '__main__':
    main()
