from itertools import product
n=int(input())
ans=[]
lst=[3,5,7]
for i in range(3,10):
    for v in product(lst,repeat=i):
        if len(set(v))==3:
            ans.append(int("".join(map(str,v))))
answer=0
for i in ans:
    if i<=n:
        answer+=1
print(answer)