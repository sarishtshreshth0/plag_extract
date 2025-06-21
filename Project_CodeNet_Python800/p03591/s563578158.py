import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s = str(readline().rstrip().decode('utf-8'))
    print("Yes" if s[:4] == "YAKI" else "No")


if __name__ == '__main__':
    solve()
