import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    def judge():
        res = True
        prev = input()
        used = set()
        used.add(prev)
        for _ in range(N - 1):
            cur = input()
            if prev[-1] != cur[0]:
                res = False
            if cur in used:
                res = False
            used.add(cur)
            prev = cur

        return res

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
