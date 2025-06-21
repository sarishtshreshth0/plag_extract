from collections import defaultdict
d = defaultdict(int) 

n = int(input()) 
A = list(map(int, input().split())) 
for i in range(n):
    d[A[i]] += 1
    d[A[i]+1] += 1
    d[A[i]-1] += 1
ans = 0
for j,k  in d.items():
    ans = max(k,ans) 
print(ans)