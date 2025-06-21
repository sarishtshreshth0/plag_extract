from collections import Counter
import math
n = int(input())
a = list(map(int,input().split()))
 
s = []

tem = 0
s.append(tem)
for i in range(n):
    tem += a[i]
    s.append(tem)
    
b = Counter(s)
c = b.values()

ans = 0
for i in c:
    ans += (i*(i-1)//2)
        
print(ans)