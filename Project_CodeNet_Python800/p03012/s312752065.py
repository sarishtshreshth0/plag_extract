n = int(input())
l = list(map(int,input().split()))

all_sum = sum(l)


minabs = float('INF')
a=all_sum
b=0
for i in range(n-2,-1,-1):
    a-=l[i+1]
    b+=l[i+1]

    target = abs(a-b)
    if(target<minabs):
        minabs=target
print(minabs)