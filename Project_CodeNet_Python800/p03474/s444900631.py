import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B = map(int, readline().split())
    s = input()
    nums = "0123456789"

    def judge():
        if s.count("-") == 1:
            if s[A] == "-":
                first, second = s.split("-")
                for c in first:
                    if c not in nums:
                        return False
                for c in second:
                    if c not in nums:
                        return False
                return True
        return False

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
