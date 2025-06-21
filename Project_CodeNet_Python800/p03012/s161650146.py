N = int(input())
W = list(map(int,input().split()))
zettaiti_dayo=[]

for i in range(1,N):
    zettaiti_dayo.append(abs(sum(W[:i])-sum(W[i:])))

print(min(zettaiti_dayo))
