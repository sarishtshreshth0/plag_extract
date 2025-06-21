N=int(input())
a=list(map(int,input().split()))

l=[0]*((10**5)+2)

for v in a:
    l[v]+=1
    l[v+1]+=1
    l[v+2]+=1

print(max(l))