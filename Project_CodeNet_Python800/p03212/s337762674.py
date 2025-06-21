n = int(input())

def dfs(cur):
    if int(cur) > n:
        return 0
    
    if all([cur.count(c) for c in '753']):
        ret = 1
    else:
        ret = 0
    
    for i in '753':    
        ret +=dfs(str(cur)+i)

    return ret 
    
print(dfs('0'))