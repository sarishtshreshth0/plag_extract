import sys


def main():
    input = sys.stdin.buffer.readline
    h, w = map(int, input().split())
    print((h * w + 1) // 2 if min(h, w) > 1 else 1)


if __name__ == "__main__":
    main()
