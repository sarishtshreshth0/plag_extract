def solve():
    n = int(input())
    print(dfs('0', n))


def dfs(s, n):
    if int(s) > n:
        return 0
    r = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        r += dfs(s+c, n)
    return r


if __name__ == '__main__':
    solve()
