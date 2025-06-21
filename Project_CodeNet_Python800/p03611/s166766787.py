import collections
N = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
ans = 0
for i in range(max(a)+1):
    ans = max(ans, c[i]+c[i-1]+c[i+1])
print(ans)