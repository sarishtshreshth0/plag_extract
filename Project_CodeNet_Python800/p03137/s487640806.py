n,m = map(int,input().split())
x = list(map(int,input().split()))
x = sorted(x,reverse=True)
dist = []
for i in range(len(x)-1):
    dist.append(x[i]-x[i+1])
dist = sorted(dist,reverse=True)
ext = n-1
for i in range(ext):
    if not dist:
        print(0)
        exit()
    dist.pop(0)
print(sum(dist))