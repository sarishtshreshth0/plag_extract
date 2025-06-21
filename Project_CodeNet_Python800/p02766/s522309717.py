r=input().split()
N=int(r[0])
K=int(r[1])
l=[]
while N>=1:
    l.append(N%K)
    N=N//K
print(len(l))