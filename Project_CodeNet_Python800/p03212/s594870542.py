from collections import Counter
ls=[]
def rec(n):
    if len(str(n))>9: return
    ls.append(n)
    rec(n*10+3)
    rec(n*10+5)
    rec(n*10+7)
n=int(input())
rec(3)
rec(5)
rec(7)
cnt=0
for l in ls:
    temp=Counter(str(l))
    if l<=n and len(temp.keys())==3:
        cnt+=1
print(cnt)