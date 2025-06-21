N,K=map(int, input().split())

list=[]
while N>=K:
    x=N%K
    N=N//K
    list.append(x)

list.append(N)
print(len(list))
