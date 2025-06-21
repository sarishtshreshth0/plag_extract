import collections

n = int(input())
a = list(map(int, input().split()))

l = [None] * n * 3
for i in range(n):
    l[i] = a[i]
    l[n+i] = a[i]-1
    l[2*n+i] = a[i]+1
    
c = collections.Counter(l)
    
print(c.most_common()[0][1])