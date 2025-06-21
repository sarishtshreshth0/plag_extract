n = int(input())
def dfs(string):
    if len(string) == len(str(n)):
        return 1 if all(k in string for k in '753') and int(''.join(string)) <= n else 0

    rec = 0
    s = '753' if len(string) != 0 and string[-1] != '0' else '0753'
    for num in s:
        string.append(num)
        rec += dfs(string)
        string.pop()

    return rec

print(dfs([]))