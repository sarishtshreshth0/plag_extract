n = int(input())
def dfs(s):
    if int(s) > n:
        return 0
    r = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        r += dfs(s + c)
    return r
print(dfs('0'))