import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    CSF = [list(map(int, input().split())) for _ in range(n - 1)]

    for i in range(n):
        if i == n - 1:
            print(0)
            break
        c, s, f = CSF[i]
        now = s + c
        for j in range(i + 1, n - 1):
            c, s, f = CSF[j]
            if now >= s:
                diff = now - s
                if diff % f == 0:
                    now += c
                else:
                    now += f - diff % f + c
            else:
                now = s + c
        print(now)


if __name__ == '__main__':
    resolve()
