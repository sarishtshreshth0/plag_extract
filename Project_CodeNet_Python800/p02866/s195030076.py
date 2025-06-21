import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 998244353


def resolve():
    n = int(input())
    D = list(map(int, input().split()))
    MAX_L = max(D) + 1
    cnt = [0] * MAX_L

    for d in D:
        cnt[d] += 1

    if cnt[0] != 1 or D[0] != 0:
        print(0)
        exit()

    res = 1
    for i in range(1, MAX_L):
        if cnt[i] == 0:
            print(0)
            break
        res *= pow(cnt[i - 1], cnt[i], mod)
        res %= mod
    else:
        print(res)


if __name__ == '__main__':
    resolve()
