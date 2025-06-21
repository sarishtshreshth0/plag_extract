from collections import Counter
n = int(input())
a = list(map(int,input().split()))

def combi(n,r):
    if n<r:
        return 0
    ans = 1
    for i in range(r):
        ans*=(n-i)
        ans/=(i+1)
    return ans

b = [0]*n
b[0]=a[0]
for i in range(1,n):
    b[i]=b[i-1]+a[i]
c = Counter(b)
c[0]+=1
k = c.keys()
sum = 0
for i in k:
    sum += combi(c[i],2)
print(int(sum))
