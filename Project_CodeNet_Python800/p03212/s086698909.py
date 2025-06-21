n = int(input())

def dfs(s):
    if int(s) <= n:
        ans = 1 if all(s.count(x) > 0 for x in "357") else 0
        for x in "357":
            ans += dfs(s+x)
    else:
        return 0
    return ans

print(dfs("0"))