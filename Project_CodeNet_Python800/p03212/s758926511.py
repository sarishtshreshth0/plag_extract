N = int(input())

def dfs(s):
    if len(s) > 0:
        if int(s) > N:
            return 0

    count = 0

    if "3" in s and "5" in s and "7" in s:
        count += 1
    
    for next_n in ["3", "5", "7"]:
        count += dfs(s + next_n)

    return count

print(dfs(""))