N = int(input())
A = [0] + list(map(int,input().split()))

for i in range(1, len(A)):
  A[i] += A[i - 1]
  
from collections import defaultdict
dic = defaultdict(int)

for i in range(len(A)):
  dic[A[i]] += 1
  
ans = 0
for n in dic.values():
  ans += (n * (n - 1)) // 2
  
print(ans)