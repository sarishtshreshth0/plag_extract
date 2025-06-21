#template
from collections import Counter
def inputlist(): return [int(i) for i in input().split()]
#template
M,D = inputlist()
count = 0
for m in range(1,M+1):
    for d in range(10,D+1):
        if d//10 < 2 or d%10 < 2:
            continue
        d10 = d//10
        d1 = d%10
        if d1*d10 == m:
            count+=1
print(count)