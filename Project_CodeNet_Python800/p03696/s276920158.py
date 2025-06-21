import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    s = input()

    l = 0
    r = 0

    for char in s:
        if char == "(":
            l += 1
        else:
            if l > 0:
                l -= 1
            else:
                r += 1
    print("(" * r + s + ")" * l)


if __name__ == '__main__':
    main()
