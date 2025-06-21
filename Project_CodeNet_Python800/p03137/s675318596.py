N,M = map(int,input().split())

x = list(map(int,input().split()))

dist = []
x.sort()
if M < N:
    print(0)
    exit()
for i in range(M-1):
    dist.append(abs(x[i+1]-x[i]))

dist.sort()

for i in range(N-1):
    dist.pop()
 
print(sum(dist))