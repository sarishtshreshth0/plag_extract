n=int(input())
#n,m,q=map(int,input().split())

use=0b000
count=0
def dfs(cur,use):
    global count
    if cur>n:
        return
    if use==0b111:
        count+=1
    dfs(10*cur+3,use|0b001)
    dfs(10*cur+5,use|0b010)
    dfs(10*cur+7,use|0b100)
dfs(0,0b000)
print(count)