a,b,c,d=map(int,input().split())
res=0
for i in range(a,b):
    if c<=i<d:
        res+=1
print(res)