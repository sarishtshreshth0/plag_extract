n=int(input())
w=list(map(int, input().split()))
res=[]
for i in range(n):
    a=sum(w[:i])
    b=sum(w[i:])
    res += [abs(a-b)]
print(min(res))