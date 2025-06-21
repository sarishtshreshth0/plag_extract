N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()

if N >= M:
    print(0)
    exit()

ruisekisa = [0]*(M-1)
for i in range(0,M-1,1):
    ruisekisa[i]=X[i+1]-X[i]

ruisekisa.sort()
print(sum(ruisekisa[0:M-N]))
