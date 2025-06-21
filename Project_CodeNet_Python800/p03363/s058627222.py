n=int(input())
l=list(map(int,input().split()))
k=dict()
d=0
k[0]=1
for i in l:
    d+=i
    if d in k:k[d]+=1
    else:k[d]=1

print(sum(x*(x-1)//2 for x in k.values()))