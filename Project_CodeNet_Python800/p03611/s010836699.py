n=int(input())
a=list(map(int,input().split()))

l=[0]*(10**5+5)
for i in a:
    l[i]+=1
p=0
for j in range(10**5):
    p=max(p,l[j]+l[j+1]+l[j+2])
print(p)