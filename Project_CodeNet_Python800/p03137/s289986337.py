n,m,*x=map(int,open(0).read().split())

if n>=m:
    print(0)
    exit(0)

x=sorted(x)

s=[]
for i in range(m-1):
    s.append(x[i+1]-x[i])
s.sort()

print(sum(s[:m-n]))