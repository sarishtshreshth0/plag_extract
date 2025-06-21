N = int(input())

def dfs(s):
    if int(s) > N:
        return 0
    if s.count("7") > 0 and s.count("5") > 0 and s.count("3") > 0:
        ret = 1
    else:
        ret = 0
    for c in "753":
        ret += dfs(s + c)
    return ret

print(dfs("0"))    