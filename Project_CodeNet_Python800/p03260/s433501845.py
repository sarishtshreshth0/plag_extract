import sys


def main():
    a, b = map(int, input().split())

    for c in range(1, 4):
        if (a * b * c) % 2 == 1:
            print('Yes')
            sys.exit(0)
    print('No')


if __name__ == "__main__":
    main()
