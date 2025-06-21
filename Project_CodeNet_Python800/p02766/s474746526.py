import sys


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    i = 1
    while k ** i <= n:
        i += 1
    print(i)


if __name__ == "__main__":
    main()
