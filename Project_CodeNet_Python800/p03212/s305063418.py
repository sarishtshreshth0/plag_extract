def dfs(s):
    if int(s) > n:
        return 0
    m = 1 if all(s.count(i) > 0 for i in "753") else 0
    for i in "753":
        m += dfs(s + i)
    return m
n = int(input())
print(dfs("0"))