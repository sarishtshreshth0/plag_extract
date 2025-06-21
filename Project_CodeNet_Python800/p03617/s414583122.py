
#q:0.25,h:0.5,s:1,d:2
#q,h,s,d=
cost=list(map(int,input().split()))

one=min(cost[0]*4,cost[1]*2,cost[2])

n=int(input())

if n==1:
    print(one)
    exit()

if n%2==0:
    print(n//2*min(one*2,cost[3]))
else:
    print(n//2*min(one*2,cost[3])+one)




