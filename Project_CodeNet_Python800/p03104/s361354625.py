a, b = map(int, input().split())

# 4つごとに区切る
def solve(n):
    m = (n // 4) * 4
    res = m
    for i in range(m + 1, n + 1):
        res ^= i
    return res

print(solve(b) ^ solve(a - 1))


