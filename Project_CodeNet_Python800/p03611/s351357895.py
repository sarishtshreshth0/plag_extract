N=int(input())
A=list(map(int,input().split()))
ans = 0
from collections import defaultdict
dic = defaultdict(int)
for i in range(N):
    dic[A[i]] += 1
    dic[A[i]+1] += 1
    dic[A[i]-1] += 1
for x in range(-1, 10**5+1):
    ans = max(ans, dic[x])
print(ans)