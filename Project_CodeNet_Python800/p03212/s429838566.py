N=int(input())
num=[3,5,7]
def dfs(s):
    if s>N:
        return 0
    a=str(s)
    if a.count("3")>=1 and a.count("5")>=1 and a.count("7")>=1:
        ret=1
    else:
        ret=0
    for i in num:
        ret+=dfs(10*s+i)
    return ret
print(dfs(0))