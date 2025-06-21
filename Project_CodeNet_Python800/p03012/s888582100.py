n=int(input())
w=list(map(int,input().split()))
result=sum(w)
for i in range(n):
    w1=sum(w[:i])
    w2=sum(w[i:])
    sa = abs(w1-w2)
    if result > sa:
        result = sa
print(result)