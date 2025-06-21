from collections import Counter
N, = list(map(int,input().split()))
a  = list(map(int,input().split()))
c  = Counter()
for ai in a:
    for b in range(ai-1,ai+2):
        c[b] += 1
print(max(c.values()))