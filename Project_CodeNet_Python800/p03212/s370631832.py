N = int(input())
enum = []

def dfs(n):
    if int(n) > N:  return
    if "3" in n and "5" in n and "7" in n:  enum.append(n)
    dfs(n + "3")
    dfs(n + "5")
    dfs(n + "7")
    
dfs("3")
dfs("5")
dfs("7")
print(len(enum))