N=int(input())
W=list(map(int,input().split()))
l=[]
s=sum(W)
for i in range(N-1):
    x=abs(2*(sum(W[0:i+1]))-s)
    l.append(x)
print(min(l))
