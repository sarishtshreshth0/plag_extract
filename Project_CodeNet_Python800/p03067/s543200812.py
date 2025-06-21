import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    print("Yes") if a < c < b or b < c < a else print("No")

if __name__ == '__main__':
    resolve()
