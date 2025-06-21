# https://atcoder.jp/contests/abc121/tasks/abc121_d

a, b = map(int, input().split())

def func(n):
    if n % 2 == 1:
        if ((n + 1) // 2) % 2 == 1:
            return 1
        return 0
    else:
        if (n // 2) % 2 == 1:
            return n ^ 1
        return n

ans = func(a - 1) ^ func(b)
print(ans)
