import collections
n=int(input())
a=sorted(list(map(int,input().split())))
c=collections.Counter(a)
counter=0
for i in range(a[0],a[n-1]+1):
    sum=c[i-1]+c[i]+c[i+1]
    if sum>counter:
        counter=sum

print(counter)
