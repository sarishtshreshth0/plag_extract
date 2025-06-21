from math import ceil

n=int(input())
lst=[]
ans=[]

for i in range(n-1):
    x,y,z=map(int,input().split())
    lst.append([x,y,z])


for i in range(n-1):
    pin=0
    for c,s,f in lst[i:]:
        xxx=max(ceil((pin-s)/f),0)
        pin=s+xxx*f+c
    
    ans.append(pin)


for i in ans:
    print(i)

print(0)