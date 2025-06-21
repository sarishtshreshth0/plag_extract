import sys
def input(): return sys.stdin.readline().strip()


def main():
    X, Y = map(int, input().split())
    print(X + Y // 2)


if __name__ == "__main__":
    main()
