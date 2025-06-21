n = int(input())
W = list(map(int,input().split()))

mins=sum(W)
for i in range(n):
    t=abs(sum(W[:i])-sum(W[i:]))
    mins = min(mins, t)
print(mins)