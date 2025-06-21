ls=[]
def rec(n):
    if len(str(n))>9: return
    ls.append(n)
    for i in [3,5,7]: rec(10*n+i)
n=int(input())
rec(0)
cnt=0
for l in ls:
    if l<=n and all(str(l).count(i)>0 for i in "357"): cnt+=1
print(cnt)