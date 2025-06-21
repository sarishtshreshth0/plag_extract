m,d=map(int,input().split())
c=0
for x in range(d+1):
    d10,d1=x//10,x%10
    if d10>=2 and d1>=2 and d10*d1<=m:c+=1
print(c)