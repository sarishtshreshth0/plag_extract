import sys


def main():
    input = sys.stdin.buffer.readline
    x = int(input())
    a, b = divmod(x, 500)
    c = b // 5
    print(1000 * a + 5 * c)


if __name__ == "__main__":
    main()
