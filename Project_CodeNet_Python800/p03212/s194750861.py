n=int(input())
lim=len(str(n))
cand=[3,5,7]
ans=[]
while cand:
    i=cand.pop()
    for j in [3,5,7]:
        k=int(str(i)+str(j))
        if k<=n:
            cand.append(k)
            if len(set(str(k)))==3:
                ans.append(k)
print(len(ans))