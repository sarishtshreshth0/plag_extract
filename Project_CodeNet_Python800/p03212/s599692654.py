n=int(input())
def dfs(s):
    if int(s)>n:
        return 0
    a=s.count("7")
    b = s.count("5")
    c = s.count("3")
    if min(a,b,c)>0:
        ans=1
    else:
        ans=0
    for c in "753":
        ans+= dfs(s+c)
    return ans

print(dfs("0"))