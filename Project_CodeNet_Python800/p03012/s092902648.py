N=int(input())
W=[int(x) for x in input().split()]
A=[abs(sum(W[:i])-sum(W[i:])) for i in range(1,N)]
print(min(A))
