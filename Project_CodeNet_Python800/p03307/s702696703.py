import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.buffer.readline().rstrip())
    print(N if N%2 == 0 else N*2)


if __name__ == '__main__':
    main()
