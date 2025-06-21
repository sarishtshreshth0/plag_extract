import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    print("Yes" if s[:4] == "YAKI" else "No")


if __name__ == '__main__':
    resolve()
