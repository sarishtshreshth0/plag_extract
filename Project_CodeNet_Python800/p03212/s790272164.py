def dfs(li):
    if int("".join(li)) > N:
        return 0
    cnt = 1 if all(i in li for i in "357") else 0
    for i in "357":
        cnt += dfs(li + [i])
    return cnt


N = int(input())
print(dfs(["0"]))
