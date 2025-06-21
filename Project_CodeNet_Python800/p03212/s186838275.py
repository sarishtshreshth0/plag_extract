n = int(input())

def dfs(s):
    if int(s) > n:
        return 0
    if all(s.count(c) for c in "753"):
        cnt =1
    else:
        cnt =0
    for t in "753":
        cnt +=dfs(s+t) 
    return cnt
    
print(dfs("0"))