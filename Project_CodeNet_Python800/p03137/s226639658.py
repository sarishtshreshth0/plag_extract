n,m = map(int, input().split())
lis = list(map(int, input().split()))

lis =sorted(lis)

if n > m:
    print(0)
    exit()
    
tmp = []
for i in range(m-1):
    tmp.append(lis[i+1] - lis[i])
    
tmp = sorted(tmp)

if n == 1:
    print(sum(tmp))
else:
    print(sum(tmp[:-(n-1)]))