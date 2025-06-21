
N = int(input())


def dfs(s):
    if int(s) > N:
        return 0

    res = 1 if all(s.count(c) > 0 for c in "357") else 0
    for c in "357":
        res += dfs(s + c)
    return res


print(dfs("0"))
