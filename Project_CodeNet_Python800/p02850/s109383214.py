n=int(input())
nextlist=[[] for _ in range(n)]
ablist=[]
for i in range(n-1):
    a,b=map(int,input().split())
    ablist.append((a,b))
    nextlist[a-1].append(b)
    nextlist[b-1].append(a)

nc=0

for i, next in enumerate(nextlist):
    tmp=len(next)
    if tmp>nc:
        nc=tmp
        nci=i+1
print(nc)

linedic={}

seen=set()
todo=[[[nci,0]],[]]
seen.add(nci)

i=0
while todo[i] != []:
    if i ==0:
        x=1
    else:
        x=0
    todo[x]=[]
    
    for to in todo[i]:
        tmp=to[1]
        k=1
        for next in nextlist[to[0]-1]:
            if not next in seen:
                if k == tmp:
                    k +=1
                seen.add(next)
                todo[x].append([next,k])
                linedic[(min(to[0],next),max(to[0],next))]=k
                k += 1
                
    i=x

for ab in ablist:
    print(linedic[ab])