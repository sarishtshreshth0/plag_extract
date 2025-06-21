N = int(input())


def dfs(x):
    if int(x) > N:
        return 0

    if all(c in x for c in '357'):
        cnt = 1
    else:
        cnt = 0
    for c in '357':
        cnt += dfs(x+c)
    return cnt


print(dfs('0'))
