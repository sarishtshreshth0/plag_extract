import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()

    if S[:4] == "YAKI":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
